import boto3
import json

def get_price_from_aws(instance_type, region="US East (N. Virginia)"):
    pricing = boto3.client("pricing", region_name="us-east-1")
    try:
        response = pricing.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {"Type": "TERM_MATCH", "Field": "instanceType", "Value": instance_type},
                {"Type": "TERM_MATCH", "Field": "location", "Value": region},
                {"Type": "TERM_MATCH", "Field": "operatingSystem", "Value": "Linux"},
                {"Type": "TERM_MATCH", "Field": "preInstalledSw", "Value": "NA"},
                {"Type": "TERM_MATCH", "Field": "tenancy", "Value": "Shared"},
                {"Type": "TERM_MATCH", "Field": "capacitystatus", "Value": "Used"},
            ],
            MaxResults=1
        )
        product = json.loads(response['PriceList'][0])
        term = list(product['terms']['OnDemand'].values())[0]
        dimension = list(term['priceDimensions'].values())[0]
        return float(dimension['pricePerUnit']['USD'])
    except Exception as e:
        print(f"[!] Error fetching price for {instance_type}: {e}")
        return 0.0

def estimate_cost(resources):
    cost_report = []
    for r in resources:
        rtype = r["type"]
        name = r["name"]
        config = r["config"]

        if rtype == "aws_instance":
            itype = config.get("instance_type", "unknown")
            cost = get_price_from_aws(itype) * 730
            cost_report.append({"name": name, "resource": rtype, "instance_type": itype, "monthly_cost": cost})

        elif rtype == "aws_nat_gateway":
            # ~ $0.045/hr => $32.85/month + data charges
            cost = 0.045 * 730
            cost_report.append({"name": name, "resource": rtype, "monthly_cost": cost})

        elif rtype == "aws_eip":
            # Free if attached; assume 1 unattached for simplicity
            cost = 0.005 * 730
            cost_report.append({"name": name, "resource": rtype, "monthly_cost": cost})

        elif rtype == "aws_vpc_peering_connection":
            # Peering itself is free, but assume 100GB transfer/month
            cost = 0.01 * 100  # $0.01 per GB
            cost_report.append({"name": name, "resource": rtype, "monthly_cost": cost})

        else:
            # Skip non-billable or unhandled resource types
            continue

    return cost_report


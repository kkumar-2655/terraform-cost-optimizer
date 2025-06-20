from src.parse_tf import parse_tf
from src.cost_estimator import estimate_cost
from src.ai_suggester import suggest_alternatives

resources_vpc = parse_tf("terraform_cost_vpc")
resources_module = parse_tf("terraform_cost_vpc_module")

resources = resources_vpc + resources_module  # ✅ List + List = OK

cost_report = estimate_cost(resources)

print("\n=== Estimated Monthly Costs ===")
for r in cost_report:
    print(f"{r['name']} ({r['resource']}): ${r['monthly_cost']:.2f}")

print("\n=== AI Suggestions ===")
print(suggest_alternatives(cost_report))


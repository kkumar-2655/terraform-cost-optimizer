# create VPC peering connection
resource "aws_vpc_peering_connection" "default" {
  count = var.is_peering_required ? 1 : 0

  vpc_id      = aws_vpc.main.id
  peer_vpc_id = data.aws_vpc.default.id

  accepter {
    allow_remote_vpc_dns_resolution = true
  }
    requester {
        allow_remote_vpc_dns_resolution = true
    }
    auto_accept = true
    tags = merge(
        var.peering_tags,
        local.common_tags,
        {
            Name = "${var.project}-${var.environment}-default-peering"
        }
    )
}
# create route for peering connection
resource "aws_route" "public_peering" {
    count = var.is_peering_required ? 1 : 0
    route_table_id         = aws_route_table.public.id
    destination_cidr_block = data.aws_vpc.default.cidr_block
    vpc_peering_connection_id = aws_vpc_peering_connection.default[count.index].id
}
resource "aws_route" "private_peering" {
    count = var.is_peering_required ? 1 : 0
    route_table_id         = aws_route_table.private.id
    destination_cidr_block = data.aws_vpc.default.cidr_block
    vpc_peering_connection_id = aws_vpc_peering_connection.default[count.index].id
}
resource "aws_route" "database_peering" {
    count = var.is_peering_required ? 1 : 0
    route_table_id         = aws_route_table.database.id
    destination_cidr_block = data.aws_vpc.default.cidr_block
    vpc_peering_connection_id = aws_vpc_peering_connection.default[count.index].id
}

resource "aws_route" "default_peering" {
    count = var.is_peering_required ? 1 : 0
    route_table_id         = data.aws_route_table.main.id
    destination_cidr_block = var.vpc_cidr_block
    vpc_peering_connection_id = aws_vpc_peering_connection.default[count.index].id
}
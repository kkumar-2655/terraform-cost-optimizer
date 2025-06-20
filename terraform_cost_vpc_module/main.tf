module "vpc" {
  source                 = "../terraform-vpc-module"
  project                = var.project
  environment            = var.environment
  public_subnets_cidr   = var.public_subnets_cidr
  private_subnets_cidr  = var.private_subnets_cidr
  database_subnets_cidr = var.database_subnets_cidr
  is_peering_required = true
}



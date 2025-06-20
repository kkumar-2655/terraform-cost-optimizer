# 🤖 Terraform Cost Optimizer (AI + AWS Pricing)

This project analyzes your AWS Terraform infrastructure, estimates monthly costs using **real-time AWS Pricing API**, and suggests **cost-saving alternatives** using **OpenAI's GPT model**.

---

## 📦 Features

- 🔍 **Parse Terraform `.tf` files** to identify AWS resources.
- 💸 **Estimate Monthly Costs**:
  - Uses **live AWS Pricing API**
  - Supports resources like:
    - EC2 (`aws_instance`)
    - NAT Gateway (`aws_nat_gateway`)
    - Elastic IP (`aws_eip`)
    - VPC Peering (estimated)
- 🧠 **AI-Based Suggestions**:
  - Uses GPT to recommend:
    - Lower-cost instance types
    - Elimination of idle resources
    - Better networking architecture
- 📁 **Modular Design**:
  - `parse_tf.py`: Extracts resources from Terraform
  - `cost_estimator.py`: Calculates cost using AWS Pricing API
  - `ai_suggester.py`: AI-powered savings recommendations

---

## 🖼️ Project Structure


terraform-cost-optimizer/
├── run_optimizer.py
├── src/
│ ├── parse_tf.py
│ ├── cost_estimator.py
│ ├── ai_suggester.py
├── pricing/aws_prices.csv # Optional fallback or sample
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Project


git clone https://github.com/kkumar-2655/terraform-cost-optimizer.git

cd terraform-cost-optimizer

✅ 2. Install Dependencies

pip install -r requirements.txt

Dependencies:

boto3
openai
python-hcl2

✅ 3. Configure AWS CLI

aws configure

✅ 4. Set OpenAI API Key

export OPENAI_API_KEY="your-openai-key"

✅ 5. Add Your Terraform Code

Place your .tf files under folders like:
terraform_cost_vpc/
terraform_cost_vpc_module/

✅ 6. Run the Optimizer
python run_optimizer.py

🧪 Example Output

=== Estimated Monthly Costs ===
web_instance (t3.micro): $7.59
nat_gw (aws_nat_gateway): $32.85
peer_to_prod (aws_vpc_peering_connection): $1.00

=== AI Suggestions ===
- Consider switching t3.micro to t3.nano if usage is low.
- NAT Gateway is costly; consider consolidating or using serverless options.

📝 Notes
This tool does not change your Terraform code — it is read-only.

You can extend support for more AWS services like RDS, ALB, S3, Lambda.

Supports parsing .tf files across multiple modules.

💡 Inspiration
Cost can grow silently in cloud infrastructure. This tool makes cost visibility and optimization suggestions proactive, not reactive — powered by AI.



import os
import hcl2

def parse_tf(directory):
    resources_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tf"):
                with open(os.path.join(root, file), "r") as f:
                    try:
                        data = hcl2.load(f)
                        resource_block = data.get("resource", {})
                        if isinstance(resource_block, list):
                           for block in resource_block:
                               for r_type, resources in block.items():
                                   for name, config in resources.items():
                                       resources_list.append({
                                           "type": r_type,
                                            "name": name,
                                            "config": config
                                       })
                        elif isinstance(resource_block, dict):
                            for r_type, blocks in resource_block.items():
                                for name, config in blocks.items():
                                    resources_list.append({
                                        "type": r_type,
                                         "name": name,
                                         "config": config
                                    })

                    except Exception as e:
                        print(f"❌ Failed to parse {file}: {e}")
    return resources_list


"""
In each DPS folder there is a .json file that contain all technical information
for deidentification. This json file is hard to read.

Therefore, each json file is rendered as a more readable markdown (MD) file.
"""

from midom.components import Protocol
from midomtoolbox.render.markdown import render_protocol


def update_protocol_md(protocol_json_in_path, md_out_path):
    """Read protocol from input file, write md rendering to output"""
    # load protocol
    with open(protocol_json_in_path, "r") as f:
        protocol = Protocol.model_validate_json(f.read())

    # render
    with open(md_out_path, "w") as f:
        f.write(render_protocol(protocol))
    print(f"Wrote md file at {md_out_path}")


if __name__ == "__main__":
    # This script will be run from the repo root, so don't use '../'

    update_protocol_md("Internal_4/Internal_4.json","Internal_4/Internal_4.md")

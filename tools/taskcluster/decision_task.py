# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def pr(builder, branch):
    return builder.craft_pr_task(branch),


def master(builder):
    return builder.craft_master_task(),


def release(builder, tag, is_staging):
    build_task = builder.craft_release_build_task(tag)
    return (
        build_task,
        # the sign task is generated by taskgraph
        # the amazon task is generated by taskgraph
        # the email notify task is generated by taskgraph
    )

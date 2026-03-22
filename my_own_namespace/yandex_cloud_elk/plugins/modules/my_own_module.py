#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This module creates a text file on remote host

version_added: "1.0.0"

description: This module creates a text file with specified content at specified path on remote host.

options:
    path:
        description: Path where the file should be created.
        required: true
        type: str
    content:
        description: Content to write to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Create a file with content
- name: Create a test file
  my_own_module:
    path: /tmp/test.txt
    content: "Hello, World!"

# Create another file
- name: Create another file
  my_own_module:
    path: /tmp/example.txt
    content: "This is example content"
'''

RETURN = r'''
path:
    description: Path to the created file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: Content written to the file.
    type: str
    returned: always
    sample: 'Hello, World!'
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    # Check if file exists and content matches
    file_exists = os.path.exists(path)
    current_content = None

    if file_exists:
        try:
            with open(path, 'r') as f:
                current_content = f.read()
        except Exception as e:
            module.fail_json(msg=f"Failed to read existing file: {str(e)}", **result)

    # Determine if changes are needed
    if not file_exists or current_content != content:
        if module.check_mode:
            result['changed'] = True
            module.exit_json(**result)

        try:
            # Ensure directory exists
            directory = os.path.dirname(path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            # Write content to file
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {str(e)}", **result)
    else:
        # File exists and content matches, no change needed
        result['changed'] = False

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
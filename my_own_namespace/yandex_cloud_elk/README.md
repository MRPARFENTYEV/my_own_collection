# Yandex Cloud ELK Collection

## Description
This collection provides custom Ansible modules and roles for file management operations.

## Modules

### my_own_module
Creates text files on remote hosts with specified content.

**Parameters:**
- `path` (required): Path where the file should be created
- `content` (required): Content to write to the file

## Roles

### create_file
A role that uses `my_own_module` to create files with configurable parameters.

**Role Variables:**
- `file_path`: Path to create the file
- `file_content`: Content to write to the file
- `display_content`: Whether to display file content after creation

## Installation
```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
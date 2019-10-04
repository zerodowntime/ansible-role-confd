# confd

Role to install and configure confd package

## Requirements

- Ansible >= 2.7

### Supported platforms

- EL
  - 7

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| confd__package_name | Package to be installed. | string | `confd` | True |
| confd__package_state | Whether to install the package or not. | string | `present` | True |
| confd__systemd_service_name | Name of the service. | string | `confd` | True |
| confd__systemd_service_state | State of the systemd service. | string | `started` | True |
| confd__systemd_service_enabled | Whether the service should start on boot. | bool | `True` | True |
| confd__confd_toml | Configuration of confd.toml file. | dict | `Check defaults/main.yml file for more info.` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**



## Example Playbook

```yaml
    - hosts: all
      become: true
      vars:
        confd__package_name: https://packages.zdt.io/confd-0.16.0-1.el7.x86_64.rpm
      roles:
        - role: zerodowntime.confd
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.

class PackageManager:
    def __init__(self):
        self.installed_packages = {}

    def install_package(self, package_name, version):
        if package_name in self.installed_packages:
            print(f"Package '{package_name}' is already installed.")
        else:
            self.installed_packages[package_name] = version
            print(f"Package '{package_name}' version {version} installed.")

    def remove_package(self, package_name):
        if package_name in self.installed_packages:
            del self.installed_packages[package_name]
            print(f"Package '{package_name}' removed.")
        else:
            print(f"Package '{package_name}' is not installed.")

    def update_package(self, package_name, new_version):
        if package_name in self.installed_packages:
            self.installed_packages[package_name] = new_version
            print(f"Package '{package_name}' updated to version {new_version}.")
        else:
            print(f"Package '{package_name}' is not installed. Install it first before updating.")

    def list_packages(self):
        if self.installed_packages:
            print("Installed packages:")
            for package_name, version in self.installed_packages.items():
                print(f"{package_name} - {version}")
        else:
            print("No packages installed.")

if __name__ == "__main__":
    pm = PackageManager()
    
    # Contoh penggunaan
    pm.install_package("numpy", "1.21.0")
    pm.install_package("pandas", "1.3.0")
    pm.list_packages()
    pm.update_package("numpy", "1.21.1")
    pm.list_packages()
    pm.remove_package("pandas")
    pm.list_packages()

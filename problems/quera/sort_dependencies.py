packages = {'pkg1': ['pkg3'], 'pkg2':['pkg3'], 'pkg3': [], 'pkg4':['pkg1', 'pkg2']}

def sort_dependencies(packages, package_name):
    dependencies = packages[package_name]
    package_dependencies = []

    for pkg in dependencies[::-1]:
        if packages[pkg]:
            for i in packages[pkg]:
                if i not in package_dependencies:
                    package_dependencies.append(i)
        package_dependencies.append(pkg)

    return package_dependencies


problem_link = "https://quera.org/problemset/136630"

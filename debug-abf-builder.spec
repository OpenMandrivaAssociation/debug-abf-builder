Name: debug-abf-builder
Version: 0.0
Release: 1
Summary: Test package for debugging abf builders
License: GPL
Group: Development/Tools
BuildArch: noarch

%description
A dummy package that just dumps information about rpm config
etc. to debug issues with the builders.
This package isn't meant to actually built.

%prep
rpm -q rpm rpm-build
rpm -qf /usr/lib/rpm/platform/noarch-linux/macros
cat /usr/lib/rpm/platform/noarch-linux/macros
echo "arch: %{_arch}"
echo "target_cpu: %{_target_cpu}"
%dump

%build

%install
echo "arch: %{_arch}"
echo "target_cpu: %{_target_cpu}"
%dump
exit 1

%files

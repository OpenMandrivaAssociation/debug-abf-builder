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
%dump

%build
rpm --showrc
# /usr/lib/rpm/macros:/usr/lib/rpm/macros.d/*.macros:/usr/lib/rpm/macros.d/macros.*:/usr/lib/rpm/platform/%{_target}/macros:/usr/lib/rpm/fileattrs/*.attr:/usr/lib/rpm/openmandriva/macros:/etc/rpm/macros.d/*.macros:/etc/rpm/macros.*:/etc/rpm/macros:/etc/rpm/%{_target}/macros:~/.rpmmacros
echo "Target: %{_target}"
ls -l /usr/lib/rpm/macros || :
ls -l /usr/lib/rpm/macros.d/*.macros || :
ls -l /usr/lib/rpm/macros.d/macros.* || :
ls -l /usr/lib/rpm/platform/%{_target}/macros || :
ls -l /usr/lib/rpm/fileattrs/*.attr || :
ls -l /usr/lib/rpm/openmandriva/macros || :
ls -l /etc/rpm/macros.d/*.macros || :
ls -l /etc/rpm/macros.* || :
ls -l /etc/rpm/macros || :
ls -l /etc/rpm/%{_target}/macros || :
ls -l ~/.rpmmacros || :
cat ~/.rpmmacros || :
grep debug /usr/lib/rpm/openmandriva/macros || :
grep install_post /usr/lib/rpm/openmandriva/macros || :

%install
echo "arch: %{_arch}"
echo "target_cpu: %{_target_cpu}"
%dump
exit 1

%files

%define __cmake_in_source_build 1
Name:		rocminfo
Version:	3.9.0
Release:	1%{?dist}
Summary:	ROCm system info utility

License:	NCSA
URL:		https://github.com/RadeonOpenCompute/rocminfo
Source0:	https://github.com/RadeonOpenCompute/rocminfo/archive/rocm-%{version}.tar.gz
Patch0:		0001-adjust-CMAKE_CXX_FLAGS.patch
Patch1:		0002-fix-buildtype-detection.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	rocm-runtime-devel >= 2.0.0
# We need python3-devel for pathfix.py
BuildRequires:	python3-devel

%description
ROCm system info utility


%prep
%autosetup -n %{name}-rocm-%{version} -p1

pathfix.py -i %{__python3} rocm_agent_enumerator

%build
mkdir build
cd build
%cmake .. -DROCM_DIR=/usr
%make_build


%install
cd build

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 rocm_agent_enumerator %{buildroot}%{_bindir}
install -p -m 0755 rocminfo %{buildroot}%{_bindir}

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Philipp Knechtges <philipp-dev@knechtges.com> - 3.9.0-0
- Version 3.9.0

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 1.0.0-7
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Tom Stellard <tstellar@redhat.com> - 1.0.0-1
- 1.0.0 Release


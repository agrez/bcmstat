%global     commit cbd2fd5a24aa82c2f0d500491266acd4e445e221
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:       bcmstat
Version:    0.5.1
Release:    1.%{commit_short}%{?dist}
Summary:    Simple Raspberry Pi command line monitoring tool
License:    GPLv2
URL:        https://github.com/MilhouseVH/%{name}
Source0:    https://github.com/MilhouseVH/%{name}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
BuildArch:	noarch
Requires:	python3


%description
Simple Raspberry Pi command line monitoring tool:
CPU fequencies (ARM, Core, h264)
Temperature (current and peak)
IRQ/s
Network Rx/Tx
System utilisation (percentage user, nice, idle etc.)
CPU load (including individual cores when available)
GPU mem usage
RAM usage (with/without swap)
Memory leak detection (D/A options - instantaneous and accumulated memory deltas)


%prep
%autosetup -n %{name}-%{commit}


%build
%if 0%{?fedora} > 29
# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
%endif


%install
rm -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__install} -p -m 0755 bcmstat.sh %{buildroot}/%{_bindir}/%{name}


%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGELOG.md README.md VERSION
%{_bindir}/%{name}


%changelog
* Sat Apr 20 2019 Vaughan <devel at agrez dot net> - 0.5.1-1.cbd2fd5
- New release
- Fix python shebang for Fedora 30

* Thu Oct 11 2018 Vaughan <devel at agrez dot net> - 0.5.0-1.3806935
- New release

* Sun Jun 24 2018 Vaughan <devel at agrez dot net> - 0.4.9-1.2fa7d07
- New release
- Git commit: 2fa7d077c11499583f4743c383943e49a61df3cd

* Fri Nov 17 2017 Vaughan <devel at agrez dot net> - 0.4.8-1.6e4d955
- New release
- Git commit: 6e4d955f4d2aef1c67601859d61f5d2d0376ec8c

* Wed Jul 12 2017 Vaughan <devel at agrez dot net> - 0.4.4-1.4a09eb6
- New release
- Git commit: 4a09eb64a752fe5030cc6ee1d39b28ed1b3c1813

* Mon Jan 02 2017 Vaughan <devel at agrez dot net> - 0.4.3-1.6d6ba36
- New release
- Git commit: 6d6ba36a3181675ff656750d8958efbe13563941

* Fri Sep 16 2016 Vaughan <devel at agrez dot net> - 0.4.2-1.9777d1d
- Initial package
- Git commit: 9777d1d50747ef8076ba9792ff27f532f9740941

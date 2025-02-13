%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	A command-line tool for auto-documenting MySQL Schema
Name:		mysqldoc
Version:	0.0.9
Release:	5
Group:		System/Servers
License:	GPL
URL:		https://code.google.com/p/mysqldoc/
Source0:	http://mysqldoc.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mysqldoc is a command-line tool for auto-documenting MySQL Schema. Output
formats include XML, HTML, and TXT. mysqldoc takes COMMENT arguments and
translates them into useful formats.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
pod2man %{name} > %{buildroot}%{_mandir}/man1/mysqldoc.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc RELEASE_HISTORY
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/mysqldoc.1*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-4mdv2011.0
+ Revision: 620426
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.9-3mdv2010.0
+ Revision: 430141
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.0.9-2mdv2009.0
+ Revision: 268227
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-1mdv2009.0
+ Revision: 196236
- import mysqldoc


* Mon Apr 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-1mdv2009.0
- initial Mandriva package

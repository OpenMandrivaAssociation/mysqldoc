%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	A command-line tool for auto-documenting MySQL Schema
Name:		mysqldoc
Version:	0.0.9
Release:	%mkrel 1
Group:		System/Servers
License:	GPL
URL:		http://code.google.com/p/mysqldoc/
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


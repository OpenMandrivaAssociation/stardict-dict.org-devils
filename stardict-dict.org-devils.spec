%define	version	2.4.2
%define rel	4
%define release %mkrel %rel
%define dict_format_version	2.4.2

Summary:	The Devil's Dictionary for StarDict 2
Name:		stardict-dict.org-devils
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-dictd_www.dict.org_devils-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
The Devil's Dictionary converted into StarDict 2 format (originally for dictd)

%prep
%setup -q -n stardict-dictd_www.dict.org_devils-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 *.ifo *.idx* *.dict.dz $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


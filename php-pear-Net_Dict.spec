%define		_class		Net
%define		_subclass	Dict
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.7
Release:	4
Summary:	Interface to the DICT protocol
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Dict/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This class provides a simple API to the DICT Protocol handling all the
network related issues and providing DICT responses in PHP datatypes
to make it easy for a developer to use DICT servers in their programs.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdv2012.0
+ Revision: 742139
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2
+ Revision: 679411
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 594496
- update to new version 1.0.7

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-2mdv2010.1
+ Revision: 468691
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 450228
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-4mdv2010.0
+ Revision: 441358
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-3mdv2009.1
+ Revision: 322376
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2009.0
+ Revision: 236978
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 136411
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdv2007.0
+ Revision: 82260
- Import php-pear-Net_Dict

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdk
- 1.0.5

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdk
- initial Mandriva package (PLD import)


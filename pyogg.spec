%define name pyogg
%define version 1.3
%define release 15

Summary: A wrapper for the Ogg libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.andrewchatham.com/pyogg/download/%{name}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(python)
Url: http://www.andrewchatham.com/pyogg/

%description
pyogg is a Python wrapper for the Ogg libraries.

There's not a whole lot you can do with this module by itself. You'll
probably also want the ogg.vorbis module, which can be found wherever
you got this.

You can now write Python programs to encode and decode Ogg Vorbis
files (encoding is quite a bit more involved). The module is
self-documenting, though I need to update quite a bit of it.

%prep
%setup -q

%build
python config_unix.py
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%files 
%doc README AUTHORS ChangeLog NEWS
%dir %{_includedir}/python?.?/pyogg/
%{_includedir}/python?.?/pyogg/pyogg.h
%py_platsitedir/*




%changelog
* Wed Nov 02 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.3-15mdv2012.0
+ Revision: 711834
- rebuild

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3-14mdv2011.0
+ Revision: 591637
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.3-13mdv2011.0
+ Revision: 441999
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.3-12mdv2009.1
+ Revision: 319585
- rebuild with python 2.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.3-11mdv2009.0
+ Revision: 259446
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-10mdv2009.0
+ Revision: 247316
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix description
- remove URL from description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.3-8mdv2007.0
+ Revision: 88139
- Import pyogg

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.3-8mdv2007.1
- update file list

* Mon Dec 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.3-7mdk
- Rebuild

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.3-6mdk
- Rebuild for new python

* Sat Sep 04 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3-5mdk
- fix URL


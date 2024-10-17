Name:      xautomation
Version:	1.09
Release:	2
Summary:   Control X from the command line
Group:     System/X11
URL:       https://hoopajoo.net/projects/xautomation.html
Source:    http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz
License:   GPLv2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xi)

%description
Control X from the command line for scripts, and do "visual scraping" to find
things on the screen. The conrol interface allows mouse movement, clicking,
button up/down, key up/down, etc, and uses the XTest extension so you don't
have the annoying problems that xse has when apps ignore sent events. The
visgrep program find images inside of images and reports the coordinates,
allowing progams to find buttons, etc, on the screen to click on.

%prep
%setup -q

%build
export LDFLAGS="-lX11"
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/pat2ppm
%{_bindir}/patextract
%{_bindir}/png2pat
%{_bindir}/rgb2pat
%{_bindir}/visgrep
%{_bindir}/xmousepos
%{_bindir}/xte
%{_mandir}/man1/pat2ppm.1*
%{_mandir}/man1/patextract.1*
%{_mandir}/man1/png2pat.1*
%{_mandir}/man1/rgb2pat.1*
%{_mandir}/man1/visgrep.1*
%{_mandir}/man1/xmousepos.1*
%{_mandir}/man1/xte.1*
%{_mandir}/man7/xautomation.7*


%changelog
* Thu Nov 11 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.03-1mdv2011.0
+ Revision: 596133
- import xautomation



# FIXME: avoid error undefined symbol: lxappearance_changed
%define _disable_ld_no_undefined 1

# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		b3e2dc866a670919991c53ecf37b971b2a6e8899
	%global commitdate	20241011
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:        Plugin to configure OpenBox inside LXAppearance
Name:           lxappearance-obconf
Version:        0.2.4
Release:        1
Group:          Graphical desktop/Other
License:        GPLv2+
Url:            https://lxde.org/
#Source0:        hhttps://sourceforge.net/projects/lxde/files/LXAppearance%20Obconf/%{name}-%{version}.tar.xz
Source0:		https://github.com/lxde/lxappearance-obconf/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:	openbox
#BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(sm)
Requires:       lxappearance >= 0.5.1
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--disable-silent-rules \
	--enable-gtk3 \
	%{nil}
%make_build 

%install
%make_install

# locales
%find_lang %{name}


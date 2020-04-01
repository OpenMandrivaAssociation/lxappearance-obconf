%define _disable_ld_no_undefined 1

Summary:        Plugin to configure OpenBox inside LXAppearance
Name:           lxappearance-obconf
Epoch:		1
Version:        0.2.3
Release:        1
Group:          Graphical desktop/Other
License:        GPLv2+
Url:            http://lxde.org/
Source0:        hhttps://sourceforge.net/projects/lxde/files/LXAppearance%20Obconf/%{name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:	openbox
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(sm)
Requires:       lxappearance >= 0.5.1
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -q
%autopatch -p1

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
# FIXME add NEWS and TODO
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/


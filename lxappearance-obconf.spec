%define distsuffix edm
Name:           lxappearance-obconf
Version:        0.0.1
Release:        %mkrel 10
Summary:        Plugin to configure OpenBox inside LXAppearance

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://lxde.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel
BuildRequires:  openbox-devel
BuildRequires:  lxappearance-devel
BuildRequires:  %{_lib}sm6-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
Requires:       lxappearance >= 0.5.0
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -q -n %{name}
# dirty hack for outdated/changing LINGUAS file
cd po
ls *.po > LINGUAS
sed -i 's/.po//g' LINGUAS

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/lxappearance/plugins/obconf.la
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
# FIXME add NEWS and TODO
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/


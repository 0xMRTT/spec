%global forgeurl https://gitlab.gnome.org/World/design/typography
%global uuid org.gnome.design.Typography
%global tag 0.2.0

Name:      typography
Version:   0.2.0
Release:   %autorelease
Summary:   GNOME Typography tool.

%forgemeta

License:   GPL-3.0-or-later
URL:       https://gitlab.gnome.org/World/design/typography
Source0:   https://gitlab.gnome.org/World/design/typography/-/archive/%{version}/typography-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Preview GNOME Typography.
  
%prep
%autosetup -n typography-%{version}


%build
%meson
%meson_build


%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files 
%license LICENSE.md
%doc README.md
%{_bindir}/%{uuid}
%{_datadir}/dbus-1/services/%{uuid}.service
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

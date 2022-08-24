%global forgeurl https://gitlab.gnome.org/chergert/schemes/
%global uuid org.gnome.Schemes.Devel
%global tag 0.1.0

Name:      schemes
Version:   0.1.0
Release:   %autorelease
Summary:   GtkSourceView style scheme creator and editor


%forgemeta

License:   GPL-3.0-or-later
URL:       %{forgeurl}
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
This application is meant to help people who need to edit GtkSourceView
style-schemes for an application or platform. Additionally, it can help
users modify existing schemes to their preference.  

%prep
%autosetup -n schemes-%{version}


%build
%meson
%meson_build


%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Schemes.desktop

%files 
%license COPYING
%{_bindir}/schemes
%{_datadir}/glib-2.0/schemas/org.gnome.Schemes.gschema.xml
%{_metainfodir}/%{uuid}.appdata.xml
%{_datadir}/applications/org.gnome.Schemes.desktop
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

%global         forgeurl https://github.com/mjakeman/extension-manager
%global         uuid com.mattjakeman.ExtensionManager

Name:      extension-manager
Version:   0.3.2
Release:   %autorelease
Summary:   A utility for browsing and installing GNOME Shell Extensions. 

%forgemeta

License:   GPL-3.0-or-later
URL:       https://github.com/mjakeman/extension-manager/
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(text-engine-0.1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

With Extension Manager you can:
* Browsing and searching extensions from extensions.gnome.org
* Installation and Removal
* Enabling and Disabling
* Updating in-app 
* Screenshots & Images
* Ratings & Comments


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/extension-manager
%{_datadir}/extension-manager
%{_datadir}/appdata/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

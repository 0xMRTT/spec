%global         forgeurl https://github.com/ADBeveridge/raider
%global         uuid com.github.ADBeveridge.Raider

Name:      raider
Version:   1.2.2
Release:   %autorelease
Summary:   A simple shredding program built for the GNOME desktop

%forgemeta

License:   GPL-3.0-or-later
URL:       https://github.com/ADBeveridge/raider
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  itstool

#Requires: shred

%description
Raider, also known as File Shredder, is a simple shredding program built for the GNOME desktop. It uses a program from the GNU Core Utilities package, included on every Linux distribution, called shred. Raider supports all the options that shred supports.


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE.md
%doc README.md
%{_bindir}/raider
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/help/*/raider/*

%changelog
%autochangelog

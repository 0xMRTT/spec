%global         forgeurl https://github.com/realmazharhussain/gdm-settings
%global         uuid io.github.realmazharhussain.GdmSettings
%global tag v0.6
Name:      gdm-settings
Version:   0.6
Release:   %autorelease
Summary:   A settings app for Gnome Login Manager (GDM)

%forgemeta

License:   AGPL-3.0-or-later
URL:       https://github.com/realmazharhussain/gdm-settings
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
  
Requires: gdm
Requires: polkit
Requires: gettext

%description
A tool for customizing GNOME Display Manager.

With User Login Manager you can:
* Import user/session settings (currently not working on Flatpak)
* Change Background/Wallpaper (Image/Color)
* Apply themes
* Font Settings 
* Top Bar Settings 
* Display settings 


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
%{_bindir}/gdm-settings
%{_datadir}/gdm-settings
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}*
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

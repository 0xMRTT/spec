%global         forgeurl https://gitlab.com/rmnvgr/metadata-cleaner/
%global         uuid fr.romainvigier.MetadataCleaner

Name:           metadata-cleaner
Version:        2.2.3
Release:        %autorelease
Summary:        View and get rid of metadatas
BuildArch:      noarch

%forgemeta

License:        GPL-3.0-or-later
URL:            https://gitlab.com/rmnvgr/metadata-cleaner/
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

%description
This tool allows you to view metadata in your files and to get rid of it, as much as possible.

%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md
%{_bindir}/metadata-cleaner 
%{python3_sitelib}/metadata-cleaner 
%{_datadir}/metadata-cleaner 
%{_datadir}/appdata/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

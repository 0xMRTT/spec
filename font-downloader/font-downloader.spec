%global forgeurl https://github.com/GustavoPeredo/font-downloader
%global uuid org.gustavoperedo.FontDownloader

Name:           font-downloader
Version:        10.0.0
Release:        %autorelease
Summary:         Download fonts from the web! 
BuildArch:      noarch

%global tag v%{version}

%forgemeta

License:        GPL-3.0-or-later
URL:            https://github.com/GustavoPeredo/Font-Downloader
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  gtk3
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(libhandy-1)

%description
Font Downloader help you download fonts on Google Font easily

%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/curtail
%{_datadir}/curtail
%{_datadir}/metainfo/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

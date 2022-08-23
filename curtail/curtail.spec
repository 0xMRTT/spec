%global         forgeurl https://github.com/Huluti/Curtail
%global         uuid com.github.huluti.Curtail

Name:           curtail
Version:        1.3.1
Release:        %autorelease
Summary:        Compress your images
BuildArch:      noarch

%global tag %{version}

%forgemeta

License:        GPL-3.0-or-later
URL:            https://github.com/Huluti/Curtail
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  gtk3
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       jpegoptim
Requires:       options
Requires:       pngquant

%description
Curtail (previously ImCompressor) is an useful image compressor, supporting PNG, JPEG and WEBP file types. It support both lossless and lossy compression modes with an option to whether keep or not metadata of images.

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

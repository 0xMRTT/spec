%global __cargo_skip_build 0
%global         forgeurl https://gitlab.gnome.org/World/Authenticator
%global         uuid com.belmoussaoui.Authenticator
%global         tag 4.1.6

Name:      authenticator
Version:   4.1.6
Release:   %autorelease
Summary:   GNOME app for generating Two-Factor Codes


ExclusiveArch: %{rust_arches}

%forgemeta

License:   GPL-3.0-or-later
URL:       https://gitlab.gnome.org/World/Authenticator
Source0:   https://gitlab.gnome.org/World/Authenticator/-/archive/%{version}/authenticator-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(zbar)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
  
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  rust-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
A tool for generating 2FA codes. Authenticator has a lot of features:
* Time-based/Counter-based/Steam methods support
* SHA-1/SHA-256/SHA-512 algorithms support
* QR code scanner using a camera or from a screenshot
* Lock the application with a password
* Beautiful UI
* GNOME Shell search provider
* Backup/Restore from/into known applications like FreeOTP+, Aegis (encrypted / plain-text), andOTP, Google Authenticator


%prep
%forgeautosetup
	
  
  
# We will build by cargo ourselves
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
sed -i -e '/dependency/d' meson.build
	
%cargo_prep
	
	
%generate_buildrequires
%cargo_generate_buildrequires
	
echo 'meson'
echo '/usr/bin/appstream-util'
echo '/usr/bin/desktop-file-validate'
	
 
	
%build
%meson
%meson_build
%cargo_build
	
	
%install
%meson_install
%cargo_install
	
# clean up buildroot pollution caused by build system errors
rm -rf %{buildroot}/builddir

 
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
	
%files
%license LICENSE.md
%doc README.md
%{_bindir}/authenticator
%{_datadir}/authenticator/*
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/locale/*/LC_MESSAGES/authenticator.mo
%{_datadir}/dbus-1/services/%{uuid}.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/%{uuid}.search-provider.ini
  
%changelog
%autochangelog

# Thanks to https://src.fedoraproject.org/rpms/newsflash/blob/f35/f/newsflash.spec

%global __cargo_skip_build 0
%global         forgeurl https://gitlab.gnome.org/World/design/icon-library
%global         uuid org.gnome.design.IconLibrary
%global         tag 0.0.12

Name:      icon-library
Version:   0.0.12
Release:   %autorelease
Summary:   GNOME symbolic icons for your apps.

ExclusiveArch: %{rust_arches}

%forgemeta

License:   GPL-3.0-or-later
URL:       https://gitlab.gnome.org/World/design/icon-library
Source0:   https://gitlab.gnome.org/World/design/icon-library/-/archive/%{version}/icon-library-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  rust-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
A tool for browsing symbolic GNOME icons, you can download icons and use them in your apps.


%prep
%autosetup -n icon-library-%{version} -p1
	
  
  
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
mv %{buildroot}%{_bindir}/{icon-library,%{uuid}}
	
# clean up buildroot pollution caused by build system errors
rm -rf %{buildroot}/builddir

 
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
	
%files
%license LICENSE.md
%doc README.md
%{_bindir}/icon-library
%{_datadir}/icon-library/*
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog

# Thanks to https://src.fedoraproject.org/rpms/newsflash/blob/f35/f/newsflash.spec

# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate sourceview5-sys

Name:           rust-sourceview5-sys
Version:        0.4.2
Release:        %autorelease
Summary:        FFI bindings for GtkSourceView 5

License:        MIT
URL:            https://crates.io/crates/sourceview5-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  pkgconfig(gtksourceview-5)

%global _description %{expand:
FFI bindings for GtkSourceView 5.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages which
use the "dox" feature of the "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v5_2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v5_2-devel %{_description}

This package contains library source intended for building other packages which
use the "v5_2" feature of the "%{crate}" crate.

%files       -n %{name}+v5_2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v5_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v5_4-devel %{_description}

This package contains library source intended for building other packages which
use the "v5_4" feature of the "%{crate}" crate.

%files       -n %{name}+v5_4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v5_6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v5_6-devel %{_description}

This package contains library source intended for building other packages which
use the "v5_6" feature of the "%{crate}" crate.

%files       -n %{name}+v5_6-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog

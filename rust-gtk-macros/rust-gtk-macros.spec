# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate gtk-macros

Name:           rust-gtk-macros
Version:        0.3.0
Release:        %autorelease
Summary:        Few macros to make gtk-rs development more convenient

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/gtk-macros
Source:         %{crates_source}

# fix doctest always failing
Patch0:        0001-fix-doctest-fail.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Few macros to make gtk-rs development more convenient.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

echo '/usr/bin/rustdoc

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install

%cargo_install

# %if %{with check}
# %check
# %cargo_test
# %endif

%changelog
%autochangelog
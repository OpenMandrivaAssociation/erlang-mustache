%global realname mustache
%global upstream mojombo
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}

Name:		erlang-%{realname}
Version:	0.1.1
Release:	1
Summary:	Mustache template engine for Erlang
Group:		Development/Erlang

License:	MIT
URL:		https://github.com/%{upstream}/%{realname}.erl
Source0:	https://github.com/%{upstream}/%{realname}.erl/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-mustache-0001-Migrate-to-a-new-Meck.patch
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar

%description
An Erlang port of Mustache for Ruby. Mustache is a framework-agnostic template
system that enforces separation of view logic from the template file. Indeed, it
is not even possible to embed logic in the template. This allows templates to be
reused across language boundaries and for other language independent uses.


%prep
%setup -qn %{realname}.erl-%{version}
%patch1 -p1 -b .new_meck


%build
%{rebar_compile}


%install
install -d %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin/
install -pm 644 ebin/* %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin/


%check
%{rebar_eunit}


%files
%doc examples/ README.md
%license LICENSE
%{_erllibdir}/%{realname}-%{version}/




%changelog
* Fri May 06 2016 neoclust <neoclust> 0.1.1-4.mga6
+ Revision: 1009758
- Rebuild post boostrap
- imported package erlang-mustache


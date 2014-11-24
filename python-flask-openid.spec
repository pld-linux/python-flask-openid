#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%global module Flask-OpenID
Summary:	OpenID support for Flask
Name:		python-flask-openid
Version:	1.2.4
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://pypi.python.org/packages/source/F/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	4ee3c1de53d27f4a8491afda1d67c665
URL:		http://github.com/mitsuhiko/flask-openid/
BuildRequires:	python-openid
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-openid
BuildRequires:	python3-setuptools
%endif
Requires:	python-openid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

This package includes the Python 2 version of the module.

%package -n python3-flask-openid
Summary:	OpenID support for Flask
Group:		Development/Libraries
Requires:	python3-openid

%description -n python3-flask-openid
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

This package includes the Python 3 version of the module.

%prep
%setup -q -n %{module}-%{version}

rm docs/_themes/.git
rm docs/_themes/.gitignore

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc docs LICENSE PKG-INFO README
%{py_sitescriptdir}/flask_openid.py[co]
%{py_sitescriptdir}/Flask_OpenID-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-flask-openid
%defattr(644,root,root,755)
%doc docs README LICENSE PKG-INFO
%{py3_sitescriptdir}/flask_openid.py*
%{py3_sitescriptdir}/Flask_OpenID-%{version}-py*.egg-info
%endif
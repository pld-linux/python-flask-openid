#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define	module Flask-OpenID
Summary:	OpenID support for Flask
Name:		python-flask-openid
Version:	1.2.4
Release:	2
License:	BSD
Group:		Development/Libraries
Source0:	http://pypi.python.org/packages/source/F/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	4ee3c1de53d27f4a8491afda1d67c665
URL:		http://github.com/mitsuhiko/flask-openid/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-flask >= 0.3
BuildRequires:	python-modules
BuildRequires:	python-openid >= 2.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-flask >= 0.3
BuildRequires:	python3-modules
BuildRequires:	python3-openid >= 2.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-openid >= 2.0
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
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
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

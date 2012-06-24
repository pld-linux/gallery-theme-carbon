%define		_theme		carbon
Summary:	Carbon Theme for Gallery2
Summary(pl):	Motyw Carbon dla Gallery2
Name:		gallery-theme-%{_theme}
Version:	1.1.1
Release:	0.2
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.mincel.com/carbon/g2-theme-%{_theme}-%{version}-blackjack.zip
# Source0-md5:	d59db6cb6daecda88617c1bf54ce5898
Patch0:		%{name}-hoverbox.patch
URL:		http://www.mincel.com/carbon/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/themes/%{_theme}

%description
I've developed Carbon theme for personal needs for Gallery 2. It is
based on Matrix theme. The theme works well in Firefox and IE6.

%description -l pl
Modu� Carbon dla Gallery 2 powsta� na w�asne potrzeby autora. Jest
oparty na motywie Matrix. Dzia�a dobrze pod Firefoksem i IE6.

%prep
%setup -q -n themes
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cd %{_theme}
cp -R * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

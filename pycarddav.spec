Summary:	pyCardDAV - CardDAV CLI client
Name:		pycarddav
Version:	0.4
Release:	1
License:	Expat/MIT License
Group:		Applications/Mail
Source0:	http://lostpackets.de/pycarddav/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	29a900555a0cb737af50c94f9ed050e3
URL:		http://lostpackets.de/pycarddav/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-requests
Requires:	python-urwid
Requires:	python-vobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyCardDAV is a simple to use CardDAV CLI client. It has built in
support for mutt's query_command but also works very well solo.

pyCardDAV consists of pycardsyncer, a program for syncing your CardDAV
resource into a local database and of pc_query, a program for querying
the local database. pyCardDAV is some ugly python code (actually, it's
not that bad anymore...) that holds together vobject, lxml, requests
and pysqlite .

Features/limitations:
- only use one address book resource at the moment
- tested against davical, owncloud and sabredav
- import the sender's address directly from mutt
- backup and import to/from .vcf files
- email addresses directly from mutt
- understands VCard 3.0
- Python 3 not compatible yet

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING NEWS pycard.conf.sample README.rst requirements.txt tests
%attr(755,root,root) %{_bindir}/pc_query
%attr(755,root,root) %{_bindir}/pycard-import
%attr(755,root,root) %{_bindir}/pycardsyncer
%dir %{py_sitescriptdir}/pycarddav
%{py_sitescriptdir}/pycarddav/*.py[co]
%{py_sitescriptdir}/pyCardDAV-%{version}-py*.egg-info

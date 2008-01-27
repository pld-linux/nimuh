Summary:	Nimuh is a game ambiented in Andalusia
Name:		nimuh
Version:	1.0
Release:	0.1
License:	Creative Commons
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
# Source0-md5:	77122ccc4bdd69a573b471894db9138a
URL:		http://www.nimuh.com/index.php?lang=en
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
Requires:	%{name}-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nimuh is a game ambiented in Andalusia. A game based in "Theseus and
the Minotaur Mazes" that will go through different andalusian
locations.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}

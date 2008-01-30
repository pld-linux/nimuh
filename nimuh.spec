Summary:	Nimuh is a game ambiented in Andalusia
Summary(pl.UTF-8):	Nimuh jest grą o Andaluzji
Name:		nimuh
Version:	1.02
Release:	0.2
License:	Creative Commons
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
# Source0-md5:	2876f237ff7f4aa50887f844bd807f23
URL:		http://www.nimuh.com/index.php?lang=en
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
Requires:	%{name}-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nimuh is a game ambiented in Andalusia. A game based in "Theseus and
the Minotaur Mazes" that will go through different andalusian
locations.

%description -l pl.UTF-8
Nimuh jest grą na temat Andaluzji. Gra jest oparta na grze "Theseus
and the Minotaur Mazes", w której gracz przemierza różne
andaluzyjskie lokacje.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc COPYING AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}


Name:       chrpath
Summary:    Modify rpath of compiled programs
Version:    0.13
Release:    3
Group:      Development/Tools
License:    GPL+
URL:        http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
Source0:    http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.




%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -fr %{buildroot}/usr/doc



%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README 
%{_bindir}/chrpath
%doc %{_mandir}/man1/chrpath.1*



# These and other macros are documented in dhd/droid-hal-device.inc

%define device hammerhead
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 5

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%define straggler_files \
file_contexts.bin \
property_contexts \
seapp_contexts \
service_contexts \
%{nil}


%include rpm/dhd/droid-hal-device.inc

# Clinic Management System

## Project Description
The Clinic Management System is a Django-based backend application designed to help clinics manage patients, doctors, and appointments efficiently.

The system provides a structured database to store and organize medical records, making it easier for clinic administrators to manage operations.

This project demonstrates backend development skills using Django, including database modeling, application structuring, and the Django admin interface.

---

## Features

### Patient Management
- Register new patients
- View patient records
- Update patient information
- Delete patient records

### Doctor Management
- Add doctor profiles
- Store specialization details
- Manage doctor contact information
- View list of available doctors

### Appointment Management
- Book appointments
- Assign patients to doctors
- Track appointment history
- Update appointment status (Pending, Completed, Cancelled)

### Admin Dashboard
- Manage patients, doctors, and appointments
- Perform CRUD operations through Django Admin


## Database Models

### Patient
Fields:
- name
- age
- gender
- phone_number
- created_at

### Doctor
Fields:
- name
- specialization
- phone_number
- email

### Appointment
Fields:
- patient (ForeignKey)
- doctor (ForeignKey)
- appointment_date
- status

Relationships:
- One patient can have many appointments
- One doctor can have many appointments
- Each appointment belongs to one patient and one doctor

---

## Technologies Used

- Python
- Django
- SQLite
- Git & GitHub

---

## Installation Guide

### 1️⃣ Clone the repository


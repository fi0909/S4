-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Bulan Mei 2024 pada 14.00
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_test`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `list_laptop`
--

CREATE TABLE `list_laptop` (
  `kode_laptop` varchar(50) NOT NULL,
  `harga_sewa` varchar(50) NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `jenis_laptop` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `list_laptop`
--

INSERT INTO `list_laptop` (`kode_laptop`, `harga_sewa`, `status`, `jenis_laptop`) VALUES
('A01', '3000', NULL, 'GTX 1080'),
('A02', '6000', NULL, 'RTX 2080'),
('A03', '5000', NULL, 'GTX 1090'),
('A04', '10000', NULL, 'Lenovo Legion S23 Ultra Pro'),
('A05', '5000', NULL, 'RTX 9090');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sewa_laptop`
--

CREATE TABLE `sewa_laptop` (
  `id_sewa` int(11) NOT NULL,
  `kode_laptop` varchar(20) NOT NULL,
  `jenis_laptop` varchar(30) NOT NULL,
  `harga_sewa` varchar(30) NOT NULL,
  `total_harga` varchar(30) DEFAULT NULL,
  `jam_mulai` time NOT NULL,
  `jam_akhir` time DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `sewa_laptop`
--

INSERT INTO `sewa_laptop` (`id_sewa`, `kode_laptop`, `jenis_laptop`, `harga_sewa`, `total_harga`, `jam_mulai`, `jam_akhir`, `created_at`) VALUES
(1, 'A01', 'GTX 1080', '3000', '50', '19:16:39', '19:17:13', '2023-12-01 19:16:39'),
(2, 'A01', 'GTX 1080', '3000', '3000', '00:53:34', '00:53:39', '2024-05-12 00:53:34'),
(3, 'A01', 'GTX 1080', '3000', '3000', '00:54:54', '12:35:58', '2024-05-12 00:54:54'),
(4, 'A03', 'GTX 1090', '5000', '5000', '16:05:06', '16:08:56', '2024-05-12 16:05:06'),
(5, 'A02', 'RTX 2080', '6000', '6000', '16:14:46', '16:17:41', '2024-05-12 16:14:46'),
(6, 'A01', 'GTX 1080', '3000', '3000', '16:17:50', '16:19:17', '2024-05-12 16:17:50'),
(7, 'A01', 'GTX 1080', '3000', '3000', '16:20:51', '16:22:47', '2024-05-12 16:20:51'),
(8, 'A01', 'GTX 1080', '3000', '3000', '16:22:58', '16:23:48', '2024-05-12 16:22:58'),
(9, 'A01', 'GTX 1080', '3000', '3000', '16:23:57', '16:24:40', '2024-05-12 16:23:57'),
(10, 'A01', 'GTX 1080', '3000', '3000', '16:28:05', '16:28:20', '2024-05-12 16:28:05'),
(11, 'A02', 'RTX 2080', '6000', '6000', '16:28:29', '16:30:53', '2024-05-12 16:28:29'),
(12, 'A01', 'GTX 1080', '3000', '3000', '16:31:01', '16:31:53', '2024-05-12 16:31:01'),
(13, 'A01', 'GTX 1080', '3000', '3000', '16:34:04', '16:35:08', '2024-05-12 16:34:04'),
(14, 'A02awd', 'RTX 2080', '6000', '6000', '16:35:21', '16:36:16', '2024-05-12 16:35:21'),
(15, 'A02', 'RTX 2080', '6000', '6000', '16:36:24', '16:40:34', '2024-05-12 16:36:24'),
(16, 'A02', 'RTX 2080', '6000', '6000', '16:39:58', '16:40:36', '2024-05-12 16:39:58'),
(17, 'A01', 'GTX 1080', '3000', '3000', '16:40:39', '16:40:49', '2024-05-12 16:40:39'),
(18, 'A03', 'GTX 1090', '5000', '5000', '16:40:47', '16:40:51', '2024-05-12 16:40:47'),
(19, 'A01', 'GTX 1080', '3000', '3000', '16:44:50', '16:47:10', '2024-05-12 16:44:50'),
(20, 'A01', 'GTX 1080', '3000', NULL, '16:47:22', '16:58:59', '2024-05-12 16:47:22'),
(21, 'A01', 'GTX 1080', '3000', NULL, '17:00:53', '17:00:58', '2024-05-12 17:00:53'),
(22, 'A01', 'GTX 1080', '3000', NULL, '17:02:43', '17:03:14', '2024-05-12 17:02:43'),
(23, 'A01', 'GTX 1080', '3000', NULL, '17:04:48', '17:04:52', '2024-05-12 17:04:48'),
(24, 'A02', 'RTX 2080', '6000', NULL, '17:06:13', '17:06:18', '2024-05-12 17:06:13'),
(25, 'A02', 'RTX 2080', '6000', NULL, '17:07:51', '17:07:55', '2024-05-12 17:07:51'),
(26, 'A02', 'RTX 2080', '6000', NULL, '17:08:58', '17:09:01', '2024-05-12 17:08:58'),
(27, 'A02', 'RTX 2080', '6000', NULL, '17:14:51', '17:15:10', '2024-05-12 17:14:51'),
(28, 'A01', 'GTX 1080', '3000', NULL, '17:19:02', '17:19:06', '2024-05-12 17:19:03'),
(29, 'A02', 'RTX 2080', '6000', NULL, '17:20:42', '17:20:46', '2024-05-12 17:20:42'),
(30, 'A02', 'RTX 2080', '6000', NULL, '17:26:05', '17:26:08', '2024-05-12 17:26:05'),
(31, 'A02', 'RTX 2080', '6000', NULL, '17:28:28', '17:28:31', '2024-05-12 17:28:28'),
(32, 'A02', 'RTX 2080', '6000', NULL, '17:29:41', '17:29:46', '2024-05-12 17:29:41'),
(33, 'A02', 'RTX 2080', '6000', NULL, '17:30:54', '17:30:57', '2024-05-12 17:30:54'),
(34, 'A02', 'RTX 2080', '6000', NULL, '17:31:52', '17:31:55', '2024-05-12 17:31:52'),
(35, 'A01', 'GTX 1080', '3000', NULL, '17:35:14', '17:35:17', '2024-05-12 17:35:14'),
(36, 'A02', 'RTX 2080', '6000', NULL, '17:38:15', '17:38:20', '2024-05-12 17:38:15'),
(37, 'A02', 'RTX 2080', '6000', NULL, '17:40:27', '17:40:31', '2024-05-12 17:40:27'),
(38, 'A03', 'GTX 1090', '5000', NULL, '17:42:57', '17:43:01', '2024-05-12 17:42:57'),
(39, 'A02', 'RTX 2080', '6000', NULL, '17:48:38', '17:48:41', '2024-05-12 17:48:38'),
(40, 'A01', 'GTX 1080', '3000', NULL, '17:50:31', '17:50:35', '2024-05-12 17:50:31'),
(41, 'A03', 'GTX 1090', '5000', NULL, '17:56:51', '17:56:54', '2024-05-12 17:56:51'),
(42, 'A03', 'GTX 1090', '5000', NULL, '17:57:07', '17:57:12', '2024-05-12 17:57:07'),
(43, 'A02', 'RTX 2080', '6000', NULL, '17:58:16', '17:58:19', '2024-05-12 17:58:16'),
(44, 'A02', 'RTX 2080', '6000', NULL, '17:59:19', '17:59:23', '2024-05-12 17:59:19'),
(45, 'A01', 'GTX 1080', '3000', NULL, '18:01:25', '18:01:28', '2024-05-12 18:01:25'),
(46, 'A02', 'RTX 2080', '6000', NULL, '18:02:15', '18:02:19', '2024-05-12 18:02:15'),
(47, 'A02', 'RTX 2080', '6000', NULL, '18:03:01', '18:03:05', '2024-05-12 18:03:01'),
(48, 'A02', 'RTX 2080', '6000', NULL, '18:03:46', '18:03:49', '2024-05-12 18:03:46'),
(49, 'A02', 'RTX 2080', '6000', NULL, '18:04:34', '18:04:37', '2024-05-12 18:04:34'),
(50, 'A02', 'RTX 2080', '6000', NULL, '18:06:32', '18:06:36', '2024-05-12 18:06:32');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `tipe_akun` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`username`, `password`, `nama`, `tipe_akun`) VALUES
('faris', '123', 'Faris', 'admin'),
('user', '123', 'User', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `list_laptop`
--
ALTER TABLE `list_laptop`
  ADD PRIMARY KEY (`kode_laptop`);

--
-- Indeks untuk tabel `sewa_laptop`
--
ALTER TABLE `sewa_laptop`
  ADD PRIMARY KEY (`id_sewa`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `sewa_laptop`
--
ALTER TABLE `sewa_laptop`
  MODIFY `id_sewa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

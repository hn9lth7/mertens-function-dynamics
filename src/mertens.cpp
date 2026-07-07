#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <climits>
#include <string>

using namespace std;

int main() {
	const int N = 10'000'000;
	const string full_path = "mertens_full.csv";
	const string plot_path = "mertens_plot.csv";
	const string extremes_path = "extremes.txt";
	const string mu_dist_path = "distribution.txt";

	vector<int> mu(N + 1);
	vector<int> primes;
	vector<bool> is_composite(N + 1, false);

	mu[1] = 1;
	for (int i = 2; i <= N; ++i) {
		if (!is_composite[i]) {
			primes.push_back(i);
			mu[i] = -1;
		}
		for (int p : primes) {
			long long ip = 1LL * i * p;
			if (ip > N) break;
			is_composite[ip] = true;
			if (i % p == 0) {
				mu[ip] = 0;
				break;
			} else {
				mu[ip] = -mu[i];
			}
		}
	}

	long long cnt_minus1 = 0, cnt_0 = 0, cnt_1 = 0;
	for (int i = 1; i <= N; ++i) {
		if (mu[i] == -1) cnt_minus1++;
		else if (mu[i] == 0) cnt_0++;
		else if (mu[i] == 1) cnt_1++;
	}
	double total = cnt_minus1 + cnt_0 + cnt_1;
	double p_minus1 = cnt_minus1 / total;
	double p_0 = cnt_0 / total;
	double p_1 = cnt_1 / total;

	ofstream mu_dist(mu_dist_path);
	mu_dist << "mu_value,count,probability\n";
	mu_dist << "-1," << cnt_minus1 << "," << p_minus1 << "\n";
	mu_dist << "0," << cnt_0 << "," << p_0 << "\n";
	mu_dist << "1," << cnt_1 << "," << p_1 << "\n";
	mu_dist.close();

	ofstream full_out(full_path);
	ofstream plot_out(plot_path);
	full_out << "n,mu,M\n";
	plot_out << "n,M\n";

	long long M = 0;
	long long max_abs = 0, max_pos = LLONG_MIN, min_neg = LLONG_MAX;
	int n_max_abs = 0, n_max_pos = 0, n_min_neg = 0;

	for (int i = 1; i <= N; ++i) {
		M += mu[i];

		full_out << i << "," << mu[i] << "," << M << "\n";

		if (i % 1000 == 0 || i == N) 
			plot_out << i << "," << M << "\n";

		if (abs(M) > max_abs) {
			max_abs = abs(M);
			n_max_abs = i;
		}
		if (M > max_pos) {
			max_pos = M;
			n_max_pos = i;
		}
		if (M < min_neg) {
			min_neg = M;
			n_min_neg = i;
		}
	}
	full_out.close();
	plot_out.close();

	ofstream extr("extremes.txt");
	extr << "n_max_abs = " << n_max_abs << ", |M| = " << max_abs << "\n";
	extr << "n_max_pos = " << n_max_pos << ", M = " << max_pos << "\n";
	extr << "n_min_neg = " << n_min_neg << ", M = " << min_neg << "\n";
	extr.close();

	cout << "Обчислення завершено (N = " << N << ")\n";
	cout << "Файли: " << full_path << ", " << plot_path << ", " << extremes_path << ", " << mu_dist_path << "\n";
	return 0;
}
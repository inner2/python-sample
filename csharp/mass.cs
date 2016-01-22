using System;

// 精密質量を計算する関数
class Mass
{
    private double atomic_weight_c = 12, atomic_weight_h =  1.00782503;
    private double atomic_weight_o = 15.9949146, atomic_weight_n = 14.003074;

    // public int element_max_c = 100, element_max_h = 120, element_max_o = 15, element_max_n = 10;
    public string formula;
    public double exactmass;
    public int num_c, num_h, num_o, num_n;
    public double rdb, delta;

    public Mass(double mz)
    {
        // 初期化
        int c_max = 100, h_max = 120, o_max = 10, n_max = 10;
        int c_min = 0, h_min = 0, o_min = 0, n_min = 0;
        double rdb_min = -1.5, rdb_max = 30;
        delta = 1;

        double mc, mh, mo, mn;
        double mass;
        double _rdb, _delta;


        // 上限値の絞り込み
        int num;
        num = (int)mz / (int)this.atomic_weight_c;
        if (num < c_max)
        {
            c_max = num + 1;
        }
        num = (int)mz / (int)this.atomic_weight_h;
        if (num < h_max)
        {
            h_max = num + 1;
        }
        num = (int)mz / (int)this.atomic_weight_o;
        if (num < o_max)
        {
            o_max = num + 1;
        }
        num = (int)mz / (int)this.atomic_weight_n;
        if (num < n_max)
        {
            n_max = num + 1;
        }


        // main loop
        for (int noc = c_min; noc < c_max; noc++)
        {
            mc = noc * this.atomic_weight_c;
            if (mc < mz + 1)
            {
                for (int noh = h_min; noh < h_max; noh++)
                {
                    mh = noh * this.atomic_weight_h;
                    if (mc + mh < mz + 1)
                    {
                        for (int noo = o_min; noo < o_max; noo++)
                        {
                            mo = noo * this.atomic_weight_o;
                            if (mc + mh + mo < mz + 1)
                            {
                                for (int non = n_min; non < n_max; non++)
                                {
                                    mn = non * this.atomic_weight_n;
                                    mass = mc + mh + mo + mo;

                                    if (mass < mz + 1 && mass > mz - 1)
                                    {
                                        _rdb = (double)(2 * noc + 2 - noh + non) / 2;
                                        if (_rdb < rdb_max && _rdb > rdb_min)
                                        {
                                            _delta = mz - mass;
                                            if (delta * delta > _delta * _delta)
                                            {
                                                this.exactmass = mass;
                                                this.delta = _delta;
                                                this.rdb = _rdb;
                                                this.num_c = noc;
                                                this.num_h = noh;
                                                this.num_o = noo;
                                                this.num_n = non;
                                                this.formula = "C" + noc + "H" + noh + "O" + noo + "N" + non;
                                            }
                                        }
                                    }

                                }  // for n
                            }  // if mo
                        }  // for o
                    }  // if mh
                }  // for h
            }  // if mc
        }  // for c
    }

		public static void Main()
		{
        Console.Write("input mass number : ");
        double input = Convert.ToDouble(Console.ReadLine());
				Mass mass = new Mass(input);
				Console.WriteLine(mass.exactmass + ":" + mass.formula + ":" + mass.delta + ":" + mass.rdb);
		}
}

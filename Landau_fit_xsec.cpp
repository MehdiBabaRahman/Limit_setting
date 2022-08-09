#include <iostream>
#include "Riostream.h"
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <math.h>
#include "TTree.h"
#include "TBranch.h"
#include "TFrame.h"
#include "TCanvas.h"
#include "TPaveLabel.h"
#include "TPaveText.h"
#include "TFile.h"
#include "TString.h"
#include "TStyle.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1.h"
#include "TF1.h"
#include "TLorentzVector.h"
#include "math.h"
#include "time.h"
#include "TRandom.h"
#include "TGraph.h"
#include "TAxis.h"
#include "TH1.h"
//#include "TSpectrum.h"
#include "TGraph.h"
#include "TMultiGraph.h"
#include <algorithm>
#include "TLine.h"
#include <TGraphErrors.h>
// #include "tdrstyle.C"
// #include "CMS_lumi.C"
#include "TH1.h"
#include "TH1F.h"
#include "TMath.h"

using namespace std;

int Landau_fit_xsec() {    

  
  TCanvas* canv = new TCanvas();


  TMultiGraph *mg = new TMultiGraph("mg","mg");
      int a = 13;
    Double_t b[13]  = {85, 95, 100, 110, 125, 130, 140, 150, 160, 170, 180, 190, 200};
    Double_t c[13]  = {1.45E+07, 2.40E+08, 6.93E+07, 2.57E+07, 1.23E+07, 1.03E+07, 7.47E+06, 5.73E+06, 4.50E+06, 3.62E+06, 2.93E+06, 2.42E+06, 2.02E+06};
    Double_t eb[13] = {};
    Double_t ec[13] = {};


   TGraphErrors *gr200 = new TGraphErrors(a,b,c, eb, ec);
   gr200->SetMarkerColor(kBlack);
   gr200->SetName("gr200");
   gr200->SetMarkerStyle(29);
   gr200->GetXaxis()->SetTitle("Prod. cross section (fb)");
   gr200->GetXaxis()->SetTitleSize(0.04);
   gr200->GetXaxis()->SetTitleOffset(1.2);
   // gr200->GetXaxis()->SetLimits(10, 400);
   gr200->GetXaxis()->SetLabelSize(0.032);
   gr200->GetXaxis()->CenterTitle(1);

   // TAxis* a = gr->GetXaxis();
   // a->SetNdivisions(510, kTRUE);
   // canv->SetLogx();

 //  gr->GetYaxis()->SetAxisRa  1E+06);
   gr200->GetYaxis()->SetTitle("c#tau (mm)");
   gr200->GetYaxis()->CenterTitle(1);
   gr200->GetYaxis()->SetTitleSize(0.04);
   gr200->GetYaxis()->SetTitleOffset(1.2);
   gr200->GetYaxis()->SetLabelSize(0.032);
   // TAxis* b = gr->GetYaxis();
   // b->SetNdivisions(507, kTRUE);
   // canv->SetLogy();
   // gr200->SetMinimum(1E-05);
   // gr200->SetMaximum(1E+05);
   gr200->SetLineColor(51);
   gr200->SetLineWidth(2);
 //  gr->SetMarkerColor(4);
   gr200->SetMarkerSize(1);

   TF1 *fit = new TF1("fit", "landau", 80 , 200);

    mg->Add( gr200 );
    gr200->Draw("ALP");
    mg->Draw("LP");
    gr200->Fit("fit", "R");

      gStyle->SetOptFit(1);
   // gStyle->SetLegendTextSize(0.03);
   // legend->Draw();
   // CMS_lumi( canv, iPeriod, iPos );
   return 0;
}


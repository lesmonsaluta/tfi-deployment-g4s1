import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import numpy as np


#Setting style for all graphs
sns.set(rc={'axes.facecolor':'white', 
            'axes.edgecolor': 'black',
            'figure.facecolor':'#ffffff',
            'grid.color': 'white',
            'text.color': 'black',
            'ytick.color': 'black',
            'xtick.color': 'black',
            'axes.labelcolor': 'black',
            'font.family': 'Arial'
            })
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

def load_data():
    # Load the data for philippines
    data = pd.read_csv(
        "micro_world.csv"
    )

    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    return philippine_data

def fin_beh():
    # Write the title and the subheader
    st.title("FINANCIAL BEHAVIORS AND ACCOUNT OWNERSHIP OF FILIPINOS")

    st.image("pexels-pixabay-259200.jpg", width = 800)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")

    subheader = '<p style="font-family:Arial; font-size: 40px; text-align: left;">What is <b>financial inclusion?</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)

    quote = '<p style="font-family:Arial; font-size: 20px;"><i>"Individuals and businesses have access to <b>useful and affordable financial products</b> that meets their needs delivered in a responsible and sustainable way." </i></p>'
    st.markdown(quote, unsafe_allow_html=True)
    source='<p style="font-family:Arial; font-size: 20px; text-align: right;"><i><b>-World Bank</b> </i></p>'
    st.markdown(source, unsafe_allow_html=True)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
    scope = '<p style="font-family:Arial; font-size: 40px; text-align: left;"><b>Scope</b></p>'
    st.markdown(scope, unsafe_allow_html=True)
    scope_text='<p style="font-family:Arial; font-size: 20px; text-align: left;"><b>Filipino respondents</b> interviewed for Global Findex Survey <b>2017.</b></p>'
    st.markdown(scope_text, unsafe_allow_html=True)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
    focus = '<p style="font-family:Arial; font-size: 40px; text-align: left;"><b>Focus</b></p>'
    st.markdown(focus, unsafe_allow_html=True)
    focus_text='<p style="font-family:Arial; font-size: 20px; text-align: left;">1. We want to know who are <b>not</b> financially included.</p><p style="font-family:Arial; font-size: 20px; text-align: left;">2. We want to <b>identify</b> financial behaviors of the financially included.</p><p style="font-family:Arial; font-size: 20px; text-align: left;">3. What can we do to <b>improve</b> their situation?</p>'
    st.markdown(focus_text, unsafe_allow_html=True)

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
    # Load data

    philippine_data = load_data()

    # Display data
    st.markdown("**The Data**")
    st.dataframe(philippine_data)
    st.markdown("Source: Global Findex 2017 from World Bank.")

    st.markdown("  ")
    st.markdown("  ")
    st.markdown("  ")
    #Partition the page into 4
    col1, col2 = st.columns(2)

    #Insert image on left side
    col1.image("3outof10.png")

    #Insert header on right side

    col2.image("6outof10.png")


def demographics():
    # Write the title
    st.title(
        "DEMOGRAPHICS OF FILIPINOS’ FINANCIAL INCLUSION"
    )

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")


    # Load data
    data = load_data()
    
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    # Fetch Philippine data
    geo_cols=["economy","economycode","regionwb"]                             
    feature_cols=["female","age","educ","inc_q","emp_in"]
    demogs_cols=feature_cols

    #FI Acesss related columns
    fi_account_cols=     ["account_fin"]



    reasons_cols=        ["fin11a","fin11b","fin11c","fin11d", "fin11e","fin11f","fin11g","fin11h"]
    reasons_cols_new=     ["Reason_too_far","Reason_too_expensive","Reason_lack_docu","Reason_lack_trust",
                            "Reason_religious","Reason_lack_money","Reason_family_has","Reason_no_need"]





    fi_account_purposes= ["fin17a","fin22a","fin27a",
                        "fin29a","fin31a","fin34a","fin39a",
                        "fin43a","fin47a"]
    fi_account_purposes_new= ["Purpose_saved","Purpose_borrowed","Purpose_sent_dom_rem",
                            "Purpose_received_dom_rem","Purpose_pay_utils","Purpose_received_wage","Purpose_received_govt_transfer",
                            "Purpose_received_agri_payment","Purpose_received_self_employment"]



    #Needed columns
    needed_cols=fi_account_cols+geo_cols+feature_cols+reasons_cols_new+fi_account_purposes_new+["wpid_random"]

    #Rename specified columns, then only include needed columns
    col_rename_dict = {i:j for i,j in zip(reasons_cols+fi_account_purposes,reasons_cols_new+fi_account_purposes_new)}
    philippine_data_2=philippine_data.rename(columns=col_rename_dict)[needed_cols]
    #philippine_data_2

    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center;"> Demographics of Financial Inclusion:<b> Income Quartile</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    col1, col2 = st.columns((1, 2))
    income = '<p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">As you  </p><p style="font-family:Arial; color:#f46524; font-size: 28px; text-align: right; margin: 0; padding-top:0;"><b>go up the income quintile,</b></p><p style="font-family:Arial; font-size: 28px; color:#f46524; text-align: right;  margin: 0; padding-top:0;"><b>the higher the proportion</b></p><p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;"> of respondents that have an account.</p>'
    col1.markdown(income, unsafe_allow_html=True)
    col2.image("image5.jpg")

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    proportion_emp_in = philippine_data_2.groupby(['emp_in']).agg(
        total_with_acc=('account_fin', 'sum'),
        total_population=('wpid_random', 'count')).reset_index()
    proportion_emp_in["Proportion"]=round(proportion_emp_in.total_with_acc*100/proportion_emp_in.total_population,2)
    #proportion_emp_in

    mapping = {
        0:'Unemployed',
        1:'Employed',

    }

    proportion_emp_in.replace({"emp_in":mapping}, inplace=True)
    #proportion_emp_in

    # Set figure size
    plt.figure(figsize=(6,3)  , dpi=200)

    label = ['Employed', 'Unemployed']
    y = np.arange(len(label))

    # Run bar plot
    fig,ax = plt.subplots()

    colors = ["#f46524", "#dedede"]
    hbar = ax.barh(
        proportion_emp_in['emp_in'],
        proportion_emp_in['Proportion'],
        color= colors
    )

    # Set title
    plt.title('Proportion of respondents with financial \n account based on employment status', fontsize=16, fontname="Arial" , y=1.1, weight="bold")
    
    # Set labels
    plt.xlabel('% Proportion')
    #plt.ylabel('Employment Status')
    plt.xlim(0, 100)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.bar_label(hbar)
    
    

    # Show figure
    show = plt.show()

    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center;"> Demographics of Financial Inclusion:<b> Employment</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    col1, col2 = st.columns([1, 2])
    unemployed = '<p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">Unemployed respondents are</p><p style="font-family:Arial; color:#f46524; font-size: 28px; text-align: right; margin: 0; padding-top:0;"><b>lesser banked</b></p><p style="font-family:Arial; font-size: 28px; text-align: right;">than employed ones, but <b>overall account ownership is still low.</b></p>'
    col1.markdown(unemployed, unsafe_allow_html=True)
    col2.pyplot(show)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    proportion_educ = philippine_data_2.groupby(['educ']).agg(
    total_with_acc=('account_fin', 'sum'),
    total_population=('wpid_random', 'count')).reset_index()
    proportion_educ["Proportion"]=round(proportion_educ.total_with_acc*100/proportion_educ.total_population,2)
    #proportion_educ

    mapping = {
        1:'Primary Education or Less',
        2:'Secondary Education',
        3:'Tertiary Education or Above',
    }

    proportion_educ.replace({"educ":mapping}, inplace=True)
    #proportion_educ

    # Set figure size
    plt.figure(figsize=(6,3)  , dpi=200)

    label = ['Tertiary Education or Above', 'Secondary Education', 'Primary Education or Less']
    y = np.arange(len(label))

    colors= ["#dedede", "#dedede", "#f46524"]

    fig, ax = plt.subplots()
    # Run bar plot
    hbar = ax.barh(
        proportion_educ['educ'],
        proportion_educ['Proportion'],
        color = colors
    )


    # Set title
    plt.title('Proportion of respondents with financial \n account based on educational attainment',
            fontsize=16, fontname="Arial",  y=1.1, weight="bold")

    # Set labels
    plt.xlabel('% Proportion')
    #plt.ylabel('Employment Status')
    plt.xlim(0, 100)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.bar_label(hbar)

    # Show figure
    show = plt.show()

    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center;">Demographics of Financial Inclusion:<b> Education</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    col1, col2 = st.columns((1, 2))
    education = '<p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">Educated respondents are banked more often.  There is an apparent correlation between</p><p style="font-family:Arial; color:#f46524; font-size: 28px; text-align: right ; margin: 0; padding-top:0;"><b>better financial literacy </b></p><p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">and</p><p style="font-family:Arial; color:#f46524; font-size: 28px; text-align: right; margin: 0; padding-top:0;"><b>higher educational attainment.</b></p>'
    col1.markdown(education, unsafe_allow_html=True)
    col2.pyplot(show)   

def fin_ex_fil():
    # Write the title and the subheader

    st.title(
        "FINANCIALLY EXCLUDED FILIPINOS"
    )

    st.image("wo_acc.png")

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: left;"><b>Main reasons</b> why Filipinos are Unbanked</p>'
    st.markdown(subheader, unsafe_allow_html=True)   
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

       # Load data
    data = load_data()
    
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    # Fetch Philippine data
    geo_cols=["economy","economycode","regionwb"]                             
    feature_cols=["female","age","educ","inc_q","emp_in"]
    demogs_cols=feature_cols

    #FI Acesss related columns
    fi_account_cols=     ["account_fin"]



    reasons_cols=        ["fin11a","fin11b","fin11c","fin11d", "fin11e","fin11f","fin11g","fin11h"]
    reasons_cols_new=     ["Reason_too_far","Reason_too_expensive","Reason_lack_docu","Reason_lack_trust",
                            "Reason_religious","Reason_lack_money","Reason_family_has","Reason_no_need"]





    fi_account_purposes= ["fin17a","fin22a","fin27a",
                        "fin29a","fin31a","fin34a","fin39a",
                        "fin43a","fin47a"]
    fi_account_purposes_new= ["Purpose_saved","Purpose_borrowed","Purpose_sent_dom_rem",
                            "Purpose_received_dom_rem","Purpose_pay_utils","Purpose_received_wage","Purpose_received_govt_transfer",
                            "Purpose_received_agri_payment","Purpose_received_self_employment"]



    #Needed columns
    needed_cols=fi_account_cols+geo_cols+feature_cols+reasons_cols_new+fi_account_purposes_new+["wpid_random"]

    #Rename specified columns, then only include needed columns
    col_rename_dict = {i:j for i,j in zip(reasons_cols+fi_account_purposes,reasons_cols_new+fi_account_purposes_new)}
    philippine_data_2=philippine_data.rename(columns=col_rename_dict)[needed_cols]
    #philippine_data_2

    unbanked_respondents = philippine_data_2[philippine_data_2['account_fin'] == 0]
    reasons_unbanked_respondents = philippine_data_2[(philippine_data_2['Reason_too_far'] == 1) |
                                            (philippine_data_2['Reason_too_expensive'] == 1) |
                                            (philippine_data_2['Reason_lack_docu'] == 1) |
                                            (philippine_data_2['Reason_lack_trust'] == 1) |
                                            (philippine_data_2['Reason_religious'] == 1) |
                                            (philippine_data_2['Reason_lack_money'] == 1) |
                                            (philippine_data_2['Reason_family_has'] == 1) |
                                            (philippine_data_2['Reason_no_need'] == 1)]

    long_reasons_unbanked = pd.melt(reasons_unbanked_respondents, 
                                    id_vars = 'account_fin',
                                    value_vars = reasons_cols_new)
    unbanked_chart_data = long_reasons_unbanked[long_reasons_unbanked['value'] == 1]\
                            .groupby(['variable']).count().reset_index().sort_values('account_fin', ascending = False)
   #unbanked_chart_data

    label = ['Lack of Money', 'Too Expensive', 'Lack Documentation', 'No Need','Bank Too Far', 'Family Has One','Lack of Trust', 'Religious Reason']

    plt.figure(figsize=(6,2), dpi=200)

    colors = ["#f46524", "#f46524", "#dedede", "#dedede", "#dedede","#dedede","#dedede", "#dedede"]
    ax = sns.barplot(
    unbanked_chart_data['account_fin'], 
    unbanked_chart_data['variable'],
    palette = colors)

    # Set title
    plt.title('Reasons for Unbankment \n (Count per respondent)',fontsize=12, y=1.1 , weight="bold", fontname='Arial')

    plt.xlabel(' ')
    plt.ylabel(' ')
    ax.set_yticklabels(label)
    ax.bar_label(ax.containers[0], fontname="Arial", fontsize=10)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.bottom.set_visible(False)
    
    show = plt.show()

    st.pyplot(show)

    caption = subheader = '<p style="font-family:Arial; font-size: 25px; text-align: left;">The most commons reasons for being unbanked are <b>lack of money</b>, and <b>expensive bank requirements</b>, which could <b>affect lower income households, who lack good financial standing.</b></p>'
    st.markdown(caption, unsafe_allow_html=True) 

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    label = ['Lack of Money', 'Too Expensive', 'Lack Documentation', 'No Need','Bank Too Far', 'Family Has One','Lack of Trust', 'Religious Reason']

    plt.figure(figsize=(6,2), dpi=200)

    colors = ["#dedede", "#dedede", "#f46524", "#f46524", "#dedede","#dedede","#dedede", "#dedede"]
    ax = sns.barplot(
    unbanked_chart_data['account_fin'], 
    unbanked_chart_data['variable'],
    palette = colors)

    # Set title
    #plt.title('Reasons for Unbankment \n (Count per respondent)',fontsize=14, y=1.1 , weight="bold", fontname='Arial')

    plt.xlabel(' ')
    plt.ylabel(' ')
    ax.set_yticklabels(label)
    ax.bar_label(ax.containers[0], fontname="Arial", fontsize=12)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.bottom.set_visible(False)
    
    show = plt.show()

    st.pyplot(show)

    caption = '<p style="font-family:Arial; font-size: 25px; text-align: left;"><b>Infrastructural reasons</b> are also common reasons why unbanked Filipinos don’t have a financial account. </p>'
    st.markdown(caption, unsafe_allow_html=True) 

def fin_in_fil():
    st.title(
        "FINANCIALLY INCLUDED FILIPINOS"
    )

    st.image("w_acc.png")

    #load the data
    data = load_data()

    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    geo_cols=["economy","economycode","regionwb"]                             
    feature_cols=["wpid_random","female","age","educ","inc_q","emp_in"]

    #FI Acesss related columns
    fi_account_cols=["account_fin"]
    reasons_cols=["fin11a","fin11b","fin11c","fin11d","fin11e","fin11f","fin11g","fin11h"]
    fi_account_purposes=["fin17a","fin22a","fin27a","fin29a","fin34a","fin39a","fin43a","fin47a"]

    #Renamed Columns
    reasons_cols_new=["Reason_too_far","Reason_too_expensive","Reason_lack_docu","Reason_lack_trust",
                    "Reason_religious","Reason_lack_money","Reason_family_has","Reason_no_need"]

    fi_account_purposes_new= ["Purpose_saved","Purpose_borrowed","Purpose_sent_dom_rem",
                          "Purpose_received_dom_rem","Purpose_received_wage","Purpose_received_govt_transfer",
                          "Purpose_received_agri_payment","Purpose_received_self_employment"]


    #Needed columns
    needed_cols=fi_account_cols+geo_cols+feature_cols+reasons_cols_new+fi_account_purposes_new

    #Rename specified columns, then only include needed columns
    col_rename_dict = {i:j for i,j in zip(reasons_cols+fi_account_purposes,reasons_cols_new+fi_account_purposes_new)}
    philippine_data_2=philippine_data.rename(columns=col_rename_dict)[needed_cols]

        #Columns Related to Purposes/Potential Use cases
    purpose_cols=["fin14a","fin14b",
                "saved","borrowed",
                "fin26","fin28",
                "fin30","fin32",
                "fin37","fin38",
                "fin42","fin46"]

    purpose_cols_new=["paid_bills_online","made_online_purchase",
                    "saved","borrowed",
                    "sent_dom_rem","rec_dom_rem",
                    "paid_utils","rec_wage",
                    "rec_govt_transfer","rec_pension",
                    "rec_agri_pay","rec_self_emp_pay"]
                    
    #Rename specified columns, then only include needed columns
    col_rename_dict_2 = {i:j for i,j in zip(purpose_cols,purpose_cols_new)}
    philippine_data_3=philippine_data.rename(columns=col_rename_dict_2)[["wpid_random"]+purpose_cols_new]
    #philippine_data_3

    #Columns- Means per action

    means_saving_cols=["fin17a","fin17b"]
    means_saving_cols_new=["saved_fin_acc","saved_inf_savings_club"]

    means_borrow_cols=["fin22a","fin22b","fin22c"]
    means_borrow_cols_new=["borrow_fin_acc","borrow_family_friends","borrow_inf_savings_club"]

    means_sdr_cols=["fin27a","fin27b","fin27c1","fin27c2"]
    means_sdr_cols_new=["sdr_fin_acc","sdr_mobile_phone","sdr_cash","sdr_mto"]

    means_rdr_cols=["fin29a","fin29b","fin29c1","fin29c2"]
    means_rdr_cols_new=["rdr_fin_acc","rdr_mobile_phone","rdr_cash","rdr_mto"]


    means_pay_utils_cols=["fin31a","fin31b","fin31c"]
    means_pay_utils_cols_new=["paid_utils_fin_acc","paid_utils_mobile_phone","paid_utils_cash"]

    means_rec_wages_cols=["fin34a","fin34b","fin34c1","fin34c2"]
    means_rec_wages_cols_new=["rec_wages_acc","rec_wages_phone","rec_wages_cash","rec_wages_card"]

    means_govt_transfers_cols=["fin39a","fin39b","fin39c1","fin39c2"]
    means_govt_transfers_cols_new=["govt_transfers_acc","govt_transfers_phone","govt_transfers_cash","govt_transfers_card"]


    means_agri_pay_cols=["fin43a","fin43b","fin43c1","fin43c2"]
    means_agri_pay_cols_new=["agri_pay_acc","agri_pay_phone","agri_pay_cash","agri_pay_card"]

    means_se_pay_cols=["fin47a","fin47b","fin47c1","fin47c2"]
    means_se_pay_cols_new=["se_pay_acc","se_pay_phone","se_pay_cash","se_pay_card"]


    all_means_cols=means_saving_cols+means_borrow_cols+means_sdr_cols+ \
                means_rdr_cols+means_pay_utils_cols+means_rec_wages_cols+ \
                means_govt_transfers_cols+means_agri_pay_cols+means_se_pay_cols
            
    all_means_cols_new=means_saving_cols_new+means_borrow_cols_new+means_sdr_cols_new+ \
                means_rdr_cols_new+means_pay_utils_cols_new+means_rec_wages_cols_new+ \
                means_govt_transfers_cols_new+means_agri_pay_cols_new+means_se_pay_cols_new

    #Rename specified columns, then only include needed columns
    col_rename_dict_3 = {i:j for i,j in zip(all_means_cols,all_means_cols_new)}
    philippine_data_4=philippine_data.rename(columns=col_rename_dict_3)[["wpid_random"]+all_means_cols_new]
    #philippine_data_4

    target_cols=["account_fin","emp_in","saved","mobileowner","borrowed","age"]
    target_cols_new=["account_fin","employed","has_credit_card","has_mobile_phone","has_nat_id","has_mobile_money_acc"]

    #3)Proper Use of Targets
    target_cols_supp=fi_account_purposes_new+ ["fin4","fin8"]
    target_cols_supp_new=fi_account_purposes_new +  ["used_debit_card", "used_credit_card"]



    #4) Type of Worker

    worker_type_cols=["fin42","fin46","fin32"]
    worker_type_cols_new=["farmers","self_emp","govt_workers"]

    col_rename_dict_4 = {i:j for i,j in zip(target_cols+target_cols_supp+worker_type_cols, 
                                            target_cols_new+target_cols_supp_new+worker_type_cols_new) }
    ph_data_r=philippine_data.rename(columns=col_rename_dict). \
                            rename(columns=col_rename_dict_2). \
                            rename(columns=col_rename_dict_3). \
                            rename(columns=col_rename_dict_4) 
            
    #ph_data_c=ph_data_r[cluster_cols]
    #ph_data_r.columns.to_list() 

    ph_data_means=philippine_data.rename(columns=col_rename_dict_2).rename(columns=col_rename_dict_3)[ ["wpid_random","account_fin"] +purpose_cols_new + all_means_cols_new]
    ph_data_means.columns.to_list()

    ph_saved=ph_data_means[(ph_data_means.saved==1) &(ph_data_means.account_fin == 1)]


    ph_saved_long=pd.melt(
    ph_saved,
        id_vars=['wpid_random','account_fin'],
        value_vars=means_saving_cols_new
    )


    ph_saved_long["adj_value"]=np.where(ph_saved_long.value==1,1,0)

    grouped=ph_saved_long.groupby(["variable","account_fin"]).agg(
        total_with_purpose=('adj_value', 'sum'),
        total_respondents=('wpid_random', 'count')).reset_index()

    grouped["Proportion"]=grouped.total_with_purpose/grouped.total_respondents*100.
    grouped=grouped.sort_values(by=["Proportion"], ascending=True).iloc[::-1]

    grouped["Proportion"] = round(grouped["Proportion"], 2)
    plt.figure(figsize=(6,3), dpi=200)

    label = ['Financial Institution', 'Informal Savings Club']
    y = np.arange(len(label))  # the label locations


    #hue_order = [1,0]
    ax = sns.barplot(
        data=grouped, 
        y="variable", 
        x="Proportion",
        orient="h",
        color = "#f46524"
        )

     # Set title
    plt.title('Means of Saving for Banked',fontsize=14, x=0.2, weight="bold", fontname='Arial')

    # Set labels
    plt.xlabel('Proportion With Savings That Used these means')
    plt.ylabel(' ')
    plt.xlim(0,100)
    ax.set_yticks(y, label)

    ax.bar_label(ax.containers[0], fontname="Arial", fontsize=12)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    #ax.yaxis.set_ticks_position('left')
    #ax.xaxis.set_ticks_position('bottom')
    #blue_patch = mpatches.Patch(color=color_banked, label='Banked')
    #yellow_patch = mpatches.Patch(color=color_unbanked, label='Unbanked')
    #plt.legend(handles=[blue_patch,yellow_patch])
    show = plt.show()

    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center; ">How banked filipinos <b>save money</b></p>'
    st.markdown(subheader, unsafe_allow_html=True) 
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    col1, col2 = st.columns((1,2))
    caption = '<p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">Majority of </p><p style="font-family:Arial; font-size: 28px; color:#f46524; text-align: right; margin: 0; padding-top:0;"><b>banked Filipinos underutilize their banks</b></p><p style="font-family:Arial; font-size: 28px; text-align: right;">for saving their money.</p>'
    col1.markdown(caption, unsafe_allow_html=True) 
    col2.pyplot(show)

    #Borrowed
    ph_borrowed=ph_data_means[(ph_data_means.borrowed==1) &(ph_data_means.account_fin == 1)]


    ph_borrowed_long=pd.melt(
    ph_borrowed,
        id_vars=['wpid_random','account_fin'],
        value_vars=means_borrow_cols_new
    )



    ph_borrowed_long["adj_value"]=np.where(ph_borrowed_long.value==1,1,0)

    grouped=ph_borrowed_long.groupby(["variable","account_fin"]).agg(
        total_with_purpose=('adj_value', 'sum'),
        total_respondents=('wpid_random', 'count')).reset_index()


    grouped["Proportion"]=grouped.total_with_purpose/grouped.total_respondents*100.
    grouped=grouped.sort_values(by=["Proportion"], ascending=False).iloc[::-1]

    grouped["Proportion"] = round(grouped["Proportion"], 2)
    plt.figure(figsize=(6,3), dpi=200)

    label = ['Family and Friends', 'Financial Institution', 'Informal Savings Club']
    y = np.arange(len(label))  # the label locations


    ax = sns.barplot(
        data=grouped.loc[::-1], 
        y="variable", 
        x="Proportion",
        orient="h",
        color = "#f46524"
        )


    # Set title
    plt.title('Means of Borrowing for Banked',fontsize=14, x=0.2, y=1.1 , weight="bold", fontname='Arial')


    # Set labels
    plt.xlabel('Proportion With Debts That Used these means')
    plt.ylabel(' ')
    plt.xlim(0,100)
    ax.set_yticks(y, label)

    ax.bar_label(ax.containers[0], fontname="Arial", fontsize=12)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    #ax.yaxis.set_ticks_position('left')
    #ax.xaxis.set_ticks_position('bottom')


    show = plt.show()
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center; ">How banked filipinos <b>borrow money</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")

    col1, col2 = st.columns((1,2))
    caption = '<p style="font-family:Arial; font-size: 25px; text-align: right; margin: 0; padding-top:0;">Similar to the unbanked,</p><p style="font-family:Arial; font-size: 25px; color:#f46524; text-align: right; margin: 0; padding-top:0;">majority of banked Filipinos <b>still rely on their family and friends</b></p><p style="font-family:Arial; font-size: 25px; text-align: right;">when borrowing money.</p><p style="font-family:Arial; font-size: 25px; text-align: right;">However, compared to the unbanked, <b>a larger proportion of banked Filipinos borrow money from financial institutions.</b></p>'
    col1.markdown(caption, unsafe_allow_html=True) 
    col2.pyplot(show)

    #UTILITY BILLS
    ph_paid_utils=ph_data_means[(ph_data_means.paid_utils==1)&(ph_data_means.account_fin == 1)]


    ph_paid_utils_long=pd.melt(
    ph_paid_utils,
        id_vars=['wpid_random','account_fin'],
        value_vars=means_pay_utils_cols_new
    )



    ph_paid_utils_long["adj_value"]=np.where(ph_paid_utils_long.value==1,1,0)

    grouped=ph_paid_utils_long.groupby(["variable","account_fin"]).agg(
        total_with_purpose=('adj_value', 'sum'),
        total_respondents=('wpid_random', 'count')).reset_index()


    grouped["Proportion"]=grouped.total_with_purpose/grouped.total_respondents*100.
    grouped=grouped.sort_values(by=["Proportion"], ascending=False).iloc[::-1]
    grouped["Proportion"] = round(grouped["Proportion"], 2)


    label = ['Cash', 'Financial Institution', 'Mobile Phone']
    y = np.arange(len(label))  # the label locations

    plt.figure(figsize=(6,3), dpi=200)

    ax = sns.barplot(
        data=grouped.loc[::-1], 
        y="variable", 
        x="Proportion",
        orient="h",
        color= "#f46524"
        )


    # Set title
    plt.title('Means of Paying Utility Bills for Banked',fontsize=14, x=0.2, y=1.1 , weight="bold", fontname='Arial')


    # Set labels
    plt.xlabel('Proportion that paid their utility bills that used these means')
    plt.ylabel(' ')
    plt.xlim(0,100)
    ax.set_yticks(y, label)

    ax.bar_label(ax.containers[0], fontname="Arial", fontsize=12)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    #ax.yaxis.set_ticks_position('left')
    #ax.xaxis.set_ticks_position('bottom')
    show = plt.show()

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    subheader = '<p style="font-family:Arial; font-size: 35px; text-align: center; ">How banked filipinos <b>pay their bills</b></p>'
    st.markdown(subheader, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")

    col1, col2 = st.columns((1,2))
    caption = '<p style="font-family:Arial; font-size: 28px; text-align: right; margin: 0; padding-top:0;">Majority of </p><p style="font-family:Arial; font-size: 28px; color:#f46524; text-align: right; margin: 0; padding-top:0;"><b>banked Filipinos underutilize their banks </b></p><p style="font-family:Arial; font-size: 28px; text-align: right;">for paying utility bills.</p>'
    col1.markdown(caption, unsafe_allow_html=True) 
    col2.pyplot(show)

def emp():
    # Write the title
    st.title(
        "On the Bright Side"
    )

def summary():
    # Write the title
    st.title(
        "Summary"
    )
    st.subheader(
        """
        Financially Excluded (Unbanked)
        1. Poorer and lower income households, respondents outside the workforce and those with lower educational attainment 
        2. Classified into the financially stable and financially insecure
        3. Financial and infrastructural reasons are holding them back from owning accounts
        """
    )
    st.subheader(
        """
        Recommendations
        1. Mitigate financial and infrastructural barriers that will make it easier for those without accounts to create accounts.
        2. Promote alternative financial institutions that are more accessible.

        """
    )
    st.subheader(
        """
        Financially Included (Banked)
        1. Classified into regular people, medically challenged, and business people
        2. Have underutilized bank accounts
        3. Prefer traditional and informal methods of saving, borrowing, and paying bills
        """
    )
    st.subheader(
        """
        Recommendations
        1. Increase awareness of different ways to borrow, save, etc, 
        2. Increase trust and confidence of the users.
        """
    )
    st.subheader(
        """
        General Recommendations
        1. 4P’s is a great opportunity to improve financial literacy of poorer and lower-income households and should be integrated in family development sessions.
        2. Continue BSP’s support for the growing and dynamic microfinance industry that has lower threshold for lending, and lower entry of barrier for poorer and lower-income households who wants access to financial institution with lower requirements compared to traditional banks.
        3. Increased digital connectivity makes financial services more accessible. Intensify coordination of BSP with DICT and fintech companies to make it convenient for an individual to register and manage an account.
        4. Trust towards banks may be low. Collect customer experience data (using incentives) to craft data-driven policies that help improve customer satisfaction, and therefore, confidence and trust in banks.
        """
    )

list_of_pages = [
    "Introduction to Financial Inclusion",
    "Demographics",
    "Financially Excluded Filipinos",
    "Financially Included  Filipinos",
    "On the Bright Side",
    "Summary"
]

st.sidebar.title('Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction to Financial Inclusion":
    fin_beh()

elif selection == "Demographics":
    demographics()

elif selection == "Financially Excluded Filipinos":
    fin_ex_fil()

elif selection == "Financially Included  Filipinos":
    fin_in_fil()

elif selection == "On the Bright Side":
    emp()

elif selection == "Summary":
    summary()
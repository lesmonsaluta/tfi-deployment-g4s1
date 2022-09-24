import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import streamlit as st


def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv"
    )

    philippine_data = data[
        data['economy'] == 'Philippines'
        ]
    return philippine_data
    

def what_is_fe():
    # Write the title and the subheader
    st.title(
        "Towards Financial Inclusion"
    )
    st.subheader(
        """
        Scope/Focus:
        1. FI metric we chose to focus on is the access to account in a financial institution (account_fin).
        2. Goal is to find out the profile of Filipinos who don’t have accounts and to find reasons as to why they don’t have accounts in a financial institution.
        """
    )

    # Load photo
    st.image("Sasa Ty-m Lab1.jpg")

    # Load data
    data = load_data()

    # Display data
    st.markdown("**The Data**")
    st.dataframe(data)
    st.markdown("Source: Global Findex 2017 from World Bank.")


def demographics():
    # Write the title
    st.title(
        "Proportion of respondents with account and without account per income quintile"
    )

    # Load data
    data = load_data()

    #Account Ownership by Income Quintiles
    accounts = data[['inc_q', 'account_fin', 'wpid_random']].reset_index().drop(columns = ['index'])
    account_chart_data = accounts.groupby(['inc_q','account_fin']).count().reset_index().pivot(index = 'account_fin',columns = 'inc_q', values = 'wpid_random')
    account_chart_data = pd.crosstab(accounts['inc_q'],
                                accounts['account_fin'],
                                normalize = 'index')
    account_chart_data['Without Account'] = round(account_chart_data[0]*100,2)
    account_chart_data['With Account'] = round(account_chart_data[1]*100,2)
    account_chart_data = account_chart_data[['Without Account', 'With Account']]

    st.markdown("As you go up the income quintile, the higher the proportion of having an account")

#Chart for Account ownership by income quintile
    fig, ax = plt.subplots(figsize=(6,4), dpi=200)
    labs = ['Poorest 20%', 'Second 20%', 'Middle 20%', 'Fourth 20%', 'Richest 20%']
    wo = ax.bar(labs, account_chart_data['Without Account'], width = .8, label='Without Account')
    w = ax.bar(labs, account_chart_data['With Account'], width = .8, bottom=account_chart_data['Without Account'],
       label='With Account')

    ax.tick_params(axis = 'x',labelrotation = 90)
    ax.set_ylabel('Proportion')
    ax.set_title('Proportion of Respondents With and Without Account by Income Quintile')
    ax.legend(bbox_to_anchor =(1.02, 0.15))
    ax.bar_label(w, label_type='center')
    ax.bar_label(wo,label_type='center')

    st.pyplot(fig)




#Rename specified columns, then only include needed columns


    # Partition the page into 2
    #col1, col2 = st.columns(2)

    # Display text in column 1
    #col1.markdown(
    #    "In the Philippines, there is still an opportunity to expand access to financial services: "
    #)

    # Display metric in column 2
    #col2.metric(
    #    label='% of Population with Debit Card',
    #    value=percent_debit_card_ownership
    #)

    # Display text
    #st.markdown("In terms of gender breakdown:")

    # Create another column for gender
    #philippine_data['gender'] = philippine_data['female'].apply(
    #    lambda x: 'male' if x == 1 else 'female'
    #)

    # Compute breakdown of access to debit card by gender
    # debit_by_gender = philippine_data.groupby('gender').agg(
    #     total_debit_card_owners=('has_debit_card', 'sum'),
    #     total_population=('wpid_random', 'count')
    # ).reset_index()

    # # Compute % debit card ownership
    # debit_by_gender['% debit card ownership'] = debit_by_gender['total_debit_card_owners'] * 100.0 / debit_by_gender[
    #     'total_population']

    # # Plot the data
    # fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
    # ax.bar(
    #     debit_by_gender["gender"],
    #     debit_by_gender["% debit card ownership"],
    # )
    # ax.set_xlabel("Gender")
    # ax.set_ylabel("% Debit Card Ownership")

    # # Show the data
    # st.pyplot(fig)


def fin_ex_fil():
    # Write the title and the subheader
    st.title(
        "Education, Employment, and Account Ownership"
    )
    st.markdown(
        "Those with lower educational attainment, as well as the unemployed have  a lower proportion of having an account. In relation to the previous slide, bigger proportions of these groups to belong to lower income quartiles."
    )

    # Load data
    data = load_data()

    #Data Wrangling
    geo_cols=["economy","economycode","regionwb"]                             
    feature_cols=["wpid_random","female","age","educ","inc_q","emp_in"]


    #FI Acesss related columns
    fi_account_cols=     ["account_fin"]
    reasons_cols=        ["fin11a","fin11b","fin11c","fin11d","fin11e","fin11f","fin11g","fin11h"]
    fi_account_purposes= ["fin17a","fin22a","fin27a","fin29a","fin34a","fin39a","fin43a","fin47a"]

    #Renamed Columns
    reasons_cols_new=        ["Reason_too_far","Reason_too_expensive","Reason_lack_docu","Reason_lack_trust",
                          "Reason_religious","Reason_lack_money","Reason_family_has","Reason_no_need"]


    fi_account_purposes_new= ["Purpose_saved","Purpose_borrowed","Purpose_sent_dom_rem",
                          "Purpose_received_dom_rem","Purpose_received_wage","Purpose_received_govt_transfer",
                          "Purpose_received_agri_payment","Purpose_received_self_employment"]

    #Needed columns
    needed_cols=fi_account_cols+geo_cols+feature_cols+reasons_cols_new+fi_account_purposes_new

    #Rename specified columns, then only include needed columns
    col_rename_dict = {i:j for i,j in zip(reasons_cols+fi_account_purposes,reasons_cols_new+fi_account_purposes_new)}
    philippine_data_2=data.rename(columns=col_rename_dict)[needed_cols].reset_index()
    proportion_educ = philippine_data_2.groupby(['educ']).agg(
    total_with_acc=('account_fin', 'sum'),
    total_population=('wpid_random', 'count')).reset_index()
    proportion_educ["Proportion"]=proportion_educ.total_with_acc/proportion_educ.total_population
    proportion_educ

    mapping = {
        1:'Primary Education or Less',
        2:'Secondary Education',
        3:'Tertiary Education or Above',
    }

    proportion_educ.replace({"educ":mapping}, inplace=True)
    proportion_educ

    # Set figure size
    plt.figure(figsize=(6,3)  , dpi=200)

    # Run bar plot
    plt.barh(
        proportion_educ['educ'],
        proportion_educ['Proportion']
    )

    # Set title
    plt.title('% With Account (Grouped by Educational Attainment)')

    # Set labels
    plt.xlabel('% Proportion')
    plt.ylabel('Education')

    # Show figure
    plt.show()


    proportion_emp_in = philippine_data_2.groupby(['emp_in']).agg(
        total_with_acc=('account_fin', 'sum'),
        total_population=('wpid_random', 'count')).reset_index()
    proportion_emp_in["Proportion"]=proportion_emp_in.total_with_acc/proportion_emp_in.total_population
    proportion_emp_in


    mapping = {
        0:'Unemployed',
        1:'Employed',

    }

    proportion_emp_in.replace({"emp_in":mapping}, inplace=True)
    proportion_emp_in


        # Set figure size
    #plt.figure(figsize=(6,3)  , dpi=200)
    fig, ax = plt.subplots(figsize=(6,4), dpi=200)
        # Run bar plot
    plt.barh(
            proportion_emp_in['emp_in'],
            proportion_emp_in['Proportion']
        )

    # Set title
    plt.title('% With Account (Grouped by Employment Status)')

    # Set labels
    plt.xlabel('% Proportion')
    plt.ylabel('Employment Status')

    # Show figure
    st.pyplot()
    # Create another column for debit card ownership
    # data['has_debit_card'] = data['fin2'].apply(
    #     lambda x: 1 if x == 1 else 0
    # )

    # # Group the data and apply aggregations
    # grouped_data = data.groupby(['economy', 'economycode', 'regionwb']).agg(
    #     total_debit_card_owners=('has_debit_card', 'sum'),
    #     total_population=('wpid_random', 'count')
    # ).reset_index()

    # # Compute debit card ownership in %
    # grouped_data['% of population with debit card'] = grouped_data['total_debit_card_owners'] * 100.0 / grouped_data[
    #     'total_population']

    # # Build the bubble map
    # fig = px.scatter_geo(
    #     grouped_data,
    #     locations="economycode",
    #     color="regionwb",
    #     hover_name="economy",
    #     size="% of population with debit card",
    #     projection="natural earth"
    # )

    # Show the figure
    #st.plotly_chart(fig)


def fin_in_fil():
    # Write the title
    st.title(
        "What We Can Do"
    )


def summary():
    # Write the title
    st.title(
        "The Team"
    )


list_of_pages = [
    "Towards Financial Inclusion",
    "Income quartiles and accounts",
    "Educ and unemployment",
    "Reasons for unbanking",
    "Digging Deeper: Reasons"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "What is Financial Exclusion":
    what_is_fe()

elif selection == "Demographics":
    demographics()

elif selection == "Financially Excluded Filipinos":
    fin_ex_fil()

elif selection == "Financially Included  Filipinos":
    fin_in_fil()

elif selection == "Summary":
    summary()


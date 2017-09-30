import Training as tr

def classify(message, training_set, prior,l):
    """
    Returns the probability that the given message is of the given type of
    the training set.
    """

    msg_terms = tr.get_words(message)

    msg_probability = 1
#using lapalace smoothing for missing term
    for term in msg_terms:
        if term in training_set:
            msg_probabilty  =msg_probability* ((training_set[term]+1)/(n+l))
        else:
            msg_probability =msg_probability* (1/(n+l))

    return msg_probability * prior


#mail_msg = input('Enter the message to be classified:')
#print('')

## 0.2 and 0.8 because the ratio of samples for spam and ham were the 0.2-0.8
n=tr.n
#spam_probability = classify(mail_msg, tr.s_t_set, 0.2,len(tr.s_t_set))
#ham_probability =classify(mail_msg, tr.h_t_set, 0.8,len(tr.h_t_set))
#if spam_probability > ham_probability:
 #   print('Your mail has been classified as SPAM.')
#else:
 #   print('Your mail has been classified as HAM.')
